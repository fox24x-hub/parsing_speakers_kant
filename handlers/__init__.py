# handlers/__init__.py
from .speakers_brief import router as speakers_brief_router
# from .other_handler import router as other_router

# Экспортируем роутеры для использования в main.py
__all__ = ['speakers_brief_router']
