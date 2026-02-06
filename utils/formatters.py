# utils/formatters.py
"""Formatting utilities for speaker data."""

def format_speaker_brief(speaker_data: dict) -> str:
    """Format speaker data for brief output.
    
    Args:
        speaker_data: Dictionary with speaker information
        
    Returns:
        Formatted string
    """
    name = speaker_data.get('name', 'Неизвестный спикер')
    description = speaker_data.get('description', 'Описание отсутствует')
    url = speaker_data.get('url', '')
    
    result = f"**{name}**\n\n"
    result += f"{description}\n"
    if url:
        result += f"\n🔗 {url}"
    
    return result
