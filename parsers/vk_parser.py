# В конец parsers/vk_parser.py
async def parse_vk_data(url: str) -> dict:
    """Parse VK speaker data from URL."""
    # Если у вас есть другая функция парсинга - используйте её
    # Это заглушка для теста
    return {
        "name": "VK Speaker",
        "url": url,
        "description": "VK profile data"
    }
