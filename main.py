import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config.settings import settings
from handlers.speakers_brief import router as speakers_brief_router

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start_handler(message: Message):
    """Обработчик команды /start"""
    await message.answer(
        "🚀 KantSpeakersBot готов!\n\n"
        "Команды:\n"
        "/topics — показать сезоны и темы\n"
        '/find_speakers winter "горные лыжи"'
    )


async def main():
    """Главная функция запуска бота"""
    # Создание экземпляра бота
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),  # HTML безопаснее для обычного текста
    )
    
    # Создание диспетчера
    dp = Dispatcher()

    # Регистрация обработчиков
    dp.message.register(start_handler, CommandStart())
    
    # Подключение роутеров
    dp.include_router(speakers_brief_router)

    # Удаление вебхука и старых обновлений
    await bot.delete_webhook(drop_pending_updates=True)
    
    logger.info("🤖 Бот запущен...")
    
    # Запуск polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
