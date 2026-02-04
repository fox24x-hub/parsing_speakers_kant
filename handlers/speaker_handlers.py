from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config.settings import settings
from parsers.youtube_parser import search_youtube_experts
from ai_analyzer.gpt_analyzer import analyze_speakers
from database.session import SessionLocal
from database.models import Speaker, ManualSpeaker
from config.topics import KANT_TOPICS

router = Router()


@router.message(Command("find_speakers"))
async def find_speakers_handler(message: Message):
    text = message.text.replace("/find_speakers", "").strip()
    parts = text.split(" ", 1)

    if len(parts) < 2:
        await message.answer(
            '❌ Формат: /find_speakers season "тема"\n'
            'Например: /find_speakers winter "горные лыжи"'
        )
        return

    season = parts[0].lower()
    topic = parts[1].strip().strip('"')

    if season not in KANT_TOPICS:
        await message.answer(
            "❌ Неизвестный сезон. Используй: winter, spring, summer, autumn.\n"
            'Например: /find_speakers winter "горные лыжи"'
        )
        return

    season_info = KANT_TOPICS[season]

    # Если тема не указана или указана общо — подставляем дефолт
    if not topic or topic.lower() in ("-", "any", "любая", "тема"):
        topic = season_info["default"]

    topics_list = ", ".join(season_info["topics"])
    await message.answer(
        f"🗓 {season_info['label']} в КАНТ.\n"
        f"Доступные темы: {topics_list}.\n"
        f"Ищу спикеров по теме: {topic}."
    )

    await message.answer(
        "🔍 Поиск спикеров КАНТ\n"
        f"Сезон: {season}\n"
        f"Тема: {topic}\n"
        "⏳ Источник: YouTube..."
    )

    # 1) автоматический поиск (YouTube)
    youtube_experts = await search_youtube_experts(
        topic=topic,
        api_key=settings.youtube_key,
        season=season,
        limit=5,
    )

    # 2) ручные спикеры из БД (ManualSpeaker)
    db = SessionLocal()
    manual_experts = []
    try:
        manual_q = (
            db.query(ManualSpeaker)
            .filter(
                ManualSpeaker.active.is_(True),
                ManualSpeaker.season == season,
                ManualSpeaker.topic == topic,
            )
            .all()
        )
        manual_experts = [
            {
                "name": m.name,
                "platform": m.platform,
                "profile_url": m.profile_url,
                "description": m.description or "",
            }
            for m in manual_q
        ]

    finally:
        db.close()

    experts = youtube_experts + manual_experts

    if not experts:
        await message.answer("😔 Не нашёл ни одного канала/спикера по этой теме.")
        return

    await message.answer("🧠 Анализирую кандидатов через GPT...")

    analyzed = await analyze_speakers(topic, season, experts)

    # Сопоставляем оценки с исходными экспертами по имени
    name_to_expert = {e["name"]: e for e in experts}

    db = SessionLocal()
    result_rows = []
    try:
        for item in analyzed:
            name = item.get("name")
            base = name_to_expert.get(name)
            if not base:
                continue

            speaker = Speaker(
                name=name,
                platform=base["platform"],
                profile_url=base["profile_url"],
                description=base.get("description", ""),
                rating=float(item.get("rating", 0)),
                recommended=bool(item.get("recommended", False)),
                season=season,
                topic=topic,
                gpt_reason=item.get("reason", ""),
            )
            db.add(speaker)
            db.flush()  # чтобы был id, если понадобится

            # Копируем данные в словарь, чтобы не зависеть от сессии
            result_rows.append(
                {
                    "name": speaker.name,
                    "platform": speaker.platform,
                    "profile_url": speaker.profile_url,
                    "rating": speaker.rating,
                    "recommended": speaker.recommended,
                    "gpt_reason": speaker.gpt_reason,
                }
            )

        db.commit()
    finally:
        db.close()

    if not result_rows:
        await message.answer("⚠️ Не удалось обработать кандидатов.")
        return

    # Берём только топ-5 по рейтингу
    top = sorted(result_rows, key=lambda x: x["rating"], reverse=True)[:5]

    lines = ["✅ Результаты анализа (топ-5):\n"]
    for i, s in enumerate(top, 1):
        mark = "✅" if s["recommended"] else "➖"
        reason_short = (s["gpt_reason"] or "")[:160]
        lines.append(f"{i}. {s['name']} ({s['platform']}) {mark}")
        lines.append(f"   ⭐ {s['rating']:.1f}")
        lines.append(f"   🔗 {s['profile_url']}")
        if reason_short:
            lines.append(f"   💬 {reason_short}")
        lines.append("")

    text = "\n".join(lines)
    if len(text) > 3500:
        text = text[:3400] + "\n\n…текст укорочен."

    # отключаем Markdown, чтобы не ловить ошибки парсинга
    await message.answer(text, parse_mode=None)
    await message.answer("💾 Спикеры сохранены в БД.")
