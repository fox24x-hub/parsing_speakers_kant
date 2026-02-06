# handlers/speakers_brief.py
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("topics"))
async def topics_handler(message: Message):
    await message.answer("Список тем...")

@router.message(Command("find_speakers"))
async def find_speakers_handler(message: Message):
    await message.answer("Поиск спикеров...")
    
"""Speaker skills mapping for different sports."""

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
