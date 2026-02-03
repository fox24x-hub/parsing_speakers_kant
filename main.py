import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config.settings import settings
from handlers.speaker_handlers import router as speakers_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_handler(message: Message):
    await message.answer(
        "🚀 KantSpeakersBot готов!\n\n"
        "Команды:\n"
        "/find_speakers winter горные лыжи"
    )

async def main():
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())
    dp.include_router(speakers_router)

    await bot.delete_webhook(drop_pending_updates=True)
    print("🤖 Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
