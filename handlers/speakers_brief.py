# handlers/speakers_brief.py
"""Handlers for speaker search and topics display."""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import logging

logger = logging.getLogger(__name__)

router = Router()

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
    try:
        topics_text = "📋 Доступные темы:\n\n"
        
        for command, info in SPEAKER_SKILLS_MAP.items():
            topics_text += f"{command} — {info['sport']} ({info['season']})\n"
        
        await message.answer(topics_text)
        logger.info(f"Topics shown to user {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in topics_handler: {e}")
        await message.answer("❌ Произошла ошибка. Попробуйте позже.")


@router.message(Command("find_speakers"))
async def find_speakers_handler(message: Message):
    """Поиск спикеров по виду спорта."""
    try:
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
        logger.info(f"Search query '{search_query}' from user {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in find_speakers_handler: {e}")
        await message.answer("❌ Произошла ошибка. Попробуйте позже.")


@router.message(Command("run_speakers"))
async def run_speakers_handler(message: Message):
    """Спикеры по бегу."""
    try:
        info = SPEAKER_SKILLS_MAP["/run_speakers"]
        await message.answer(f"🏃 Спикеры по теме: {info['sport']}")
        logger.info(f"Run speakers shown to user {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in run_speakers_handler: {e}")
