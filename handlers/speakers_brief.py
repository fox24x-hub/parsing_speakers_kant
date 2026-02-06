# handlers/speakers_brief.py
"""Handlers for speaker search and topics display."""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# Создаем роутер
router = Router()

# Маппинг навыков спикеров для разных видов спорта
SPEAKER_SKILLS_MAP = {
    "/xc_ski_speakers": {
        "sport": "Беговые лыжи",
        "skill": "xc-ski",
        "season": "зима"
    },
    "/alpine_speakers": {
        "sport": "Горные лыжи",
        "skill": "alpine",
        "season": "зима"
    },
    "/snowboard_speakers": {
        "sport": "Сноуборд",
        "skill": "snowboard",
        "season": "зима"
    },
    "/run_speakers": {
        "sport": "Бег",
        "skill": "run",
        "season": "всесезон"
    },
    "/trailrun_speakers": {
        "sport": "Трейлраннинг",
        "skill": "trailrun",
        "season": "весна-осень"
    },
    "/cycling_speakers": {
        "sport": "Велоспорт",
        "skill": "cycling",
        "season": "весна-осень"
    },
    "/swim_speakers": {
        "sport": "Плавание",
        "skill": "swim",
        "season": "всесезон"
    },
    "/hiking_speakers": {
        "sport": "Пеший туризм",
        "skill": "hiking",
        "season": "весна-осень"
    },
}


@router.message(Command("topics"))
async def topics_handler(message: Message):
    """Показывает доступные темы и виды спорта."""
    topics_text = "📋 Доступные темы:\n\n"
    
    for command, info in SPEAKER_SKILLS_MAP.items():
        topics_text += f"{command} — {info['sport']} ({info['season']})\n"
    
    await message.answer(topics_text)


@router.message(Command("find_speakers"))
async def find_speakers_handler(message: Message):
    """Поиск спикеров по виду спорта."""
    # Получаем аргументы команды
    args = message.text.split(maxsplit=1)
    
    if len(args) < 2:
        await message.answer(
            "❌ Укажите вид спорта.\n"
            "Пример: /find_speakers alpine\n\n"
            "Используйте /topics для списка доступных видов спорта."
        )
        return
    
    search_query = args[1].lower()
    await message.answer(f"🔍 Поиск спикеров по запросу: {search_query}")


# Хэндлеры для каждого вида спорта
@router.message(Command("xc_ski_speakers"))
async def xc_ski_speakers_handler(message: Message):
    """Спикеры по беговым лыжам."""
    info = SPEAKER_SKILLS_MAP["/xc_ski_speakers"]
    await message.answer(f"⛷ Спикеры по теме: {info['sport']}")


@router.message(Command("alpine_speakers"))
async def alpine_speakers_handler(message: Message):
    """Спикеры по горным лыжам."""
    info = SPEAKER_SKILLS_MAP["/alpine_speakers"]
    await message.answer(f"🎿 Спикеры по теме: {info['sport']}")


@router.message(Command("snowboard_speakers"))
async def snowboard_speakers_handler(message: Message):
    """Спикеры по сноуборду."""
    info = SPEAKER_SKILLS_MAP["/snowboard_speakers"]
    await message.answer(f"🏂 Спикеры по теме: {info['sport']}")


@router.message(Command("run_speakers"))
async def run_speakers_handler(message: Message):
    """Спикеры по бегу."""
    info = SPEAKER_SKILLS_MAP["/run_speakers"]
    await message.answer(f"🏃 Спикеры по теме: {info['sport']}")


@router.message(Command("trailrun_speakers"))
async def trailrun_speakers_handler(message: Message):
    """Спикеры по трейлраннингу."""
    info = SPEAKER_SKILLS_MAP["/trailrun_speakers"]
    await message.answer(f"🏔 Спикеры по теме: {info['sport']}")


@router.message(Command("cycling_speakers"))
async def cycling_speakers_handler(message: Message):
    """Спикеры по велоспорту."""
    info = SPEAKER_SKILLS_MAP["/cycling_speakers"]
    await message.answer(f"🚴 Спикеры по теме: {info['sport']}")


@router.message(Command("swim_speakers"))
async def swim_speakers_handler(message: Message):
    """Спикеры по плаванию."""
    info = SPEAKER_SKILLS_MAP["/swim_speakers"]
    await message.answer(f"🏊 Спикеры по теме: {info['sport']}")


@router.message(Command("hiking_speakers"))
async def hiking_speakers_handler(message: Message):
    """Спикеры по пешему туризму."""
    info = SPEAKER_SKILLS_MAP["/hiking_speakers"]
    await message.answer(f"🥾 Спикеры по теме: {info['sport']}")
