import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config.settings import settings
from handlers import speaker_handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start_handler(message: Message):
    await message.answer(
        "🚀 KantSpeakersBot готов!\n\n"
        "Команды:\n"
        "/topics — показать сезоны и темы\n"
        "/find_speakers winter \"горные лыжи\"",
        parse_mode=None,  # чтобы не ругался Markdown
    )


async def main():
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())
    dp.include_router(speaker_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    print("🤖 Бот запущен...")
    await dp.start_polling(bot)  # у оригинального Dispatcher этот метод есть [][]


if __name__ == "__main__":
    asyncio.run(main())
