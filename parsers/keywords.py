# parsers/keywords.py

TOPIC_KEYWORDS = {
    "горные лыжи": [
        "горные лыжи",
        "горнолыжный инструктор",
        "горнолыжная школа",
        "ski school",
        "ski academy",
        "skiing tutorials",
    ],
    "сноуборд": [
        "сноуборд",
        "snowboard school",
        "snowboard instructor",
        "snowboarding tutorials",
    ],
    "беговые лыжи": [
        "беговые лыжи",
        "лыжные гонки",
        "cross-country skiing",
        "xc ski training",
        "ski marathon",
    ],
# parsers/keywords.py
"""Keyword extraction utilities."""

def extract_keywords(text: str, max_keywords: int = 10) -> list[str]:
    """Extract keywords from text.
    
    Args:
        text: Input text
        max_keywords: Maximum number of keywords to return
        
    Returns:
        List of keywords
    """
    # Простая реализация - разделение по словам
    # Можно улучшить с помощью NLTK или spaCy
    words = text.lower().split()
    # Убрать служебные слова (стоп-слова)
    stop_words = {'и', 'в', 'на', 'с', 'по', 'для', 'как', 'что', 'это', 'the', 'a', 'an', 'in', 'on', 'at'}
    keywords = [w for w in words if w not in stop_words and len(w) > 3]
    return keywords[:max_keywords]    
    "трейлраннинг": [
        "трейлраннинг",
        "trail running",
        "trail running coach",
        "trail running channel",
        "ultra running",
    ],
    "триатлон": [
        "триатлон",
        "triathlon",
        "triathlon coach",
        "triathlon training",
        "ironman triathlon",
    ],
    "походы": [
        "походы",
        "hiking",
        "hiking Russia",
        "backpacking",
        "походы в горы",
        "трекинг",
    ],
}
