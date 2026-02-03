from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config.settings import settings
from parsers.youtube_parser import search_youtube_experts

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

    season = parts[0]
    topic = parts[1].strip().strip('"')

    await message.answer(
        f"🔍 Поиск спикеров КАНТ\n"
        f"Сезон: {season}\n"
        f"Тема: {topic}\n"
        f"⏳ Источник: YouTube..."
    )

    experts = await search_youtube_experts(topic, settings.youtube_key, limit=3)

    if not experts:
        await message.answer("😔 Не нашёл ни одного канала по этой теме.")
        return

    lines = ["✅ Нашёл таких кандидатов:\n"]
    for i, e in enumerate(experts, 1):
        lines.append(f"{i}. {e['name']}")
        lines.append(f"   🔗 {e['profile_url']}")
        if e.get("description"):
            lines.append(f"   ℹ️ {e['description'][:120]}...")
        lines.append("")

    await message.answer("\n".join(lines))
