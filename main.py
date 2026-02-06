import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ErrorEvent

from config.settings import settings
from handlers.speakers_brief import router as speakers_brief_router

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def start_handler(message: Message):
    """Обработчик команды /start"""
    try:
        text = (
            "🚀 KantSpeakersBot готов!\n\n"
            "Команды:\n"
            "/topics — показать все виды спорта\n"
            "/run_speakers — спикеры по бегу\n"
            "/alpine_speakers — спикеры по горным лыжам\n"
            "/xc_ski_speakers — спикеры по беговым лыжам"
        )
        # Отключаем parse_mode для избежания ошибок парсинга
        await message.answer(text, parse_mode=None)
        logger.info(f"Start command from user {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in start_handler: {e}")


async def error_handler(event: ErrorEvent):
    """Глобальный обработчик ошибок"""
    logger.error(f"Critical error: {event.exception}", exc_info=True)


async def main():
    """Главная функция запуска бота"""
    try:
        bot = Bot(
            token=settings.bot_token,
            default=DefaultBotProperties(parse_mode=None),  # Отключаем parse_mode по умолчанию
        )
        
        dp = Dispatcher()
        dp.error.register(error_handler)
        dp.message.register(start_handler, CommandStart())
        dp.include_router(speakers_brief_router)

        await bot.delete_webhook(drop_pending_updates=True)
        
        bot_info = await bot.get_me()
        logger.info(f"🤖 Бот запущен: @{bot_info.username}")
        
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
