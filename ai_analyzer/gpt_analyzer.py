from typing import List, Dict
import json
import asyncio
from openai import OpenAI
from config.settings import settings

SYSTEM_PROMPT = """
Ты помогаешь выбирать спикеров для лектория спортивного магазина КАНТ.
КАНТ продаёт: горные лыжи, сноуборд, беговые лыжи, туристическое снаряжение, бег, трейлраннинг, велосипед, плавание, триатлон.

Оценивай спикера по:
1) Релевантность теме (технические знания, опыт).
2) Публичность и умение объяснять.
3) Полезность для аудитории КАНТ.

Верни краткий JSON без комментариев.
"""

client = OpenAI(api_key=settings.openai_api_key)


def _call_openai_sync(topic: str, season: str, experts: List[Dict]) -> List[Dict]:
    if not experts:
        return []

    desc = []
    for i, e in enumerate(experts, 1):
        desc.append(
            f"{i}. Имя: {e['name']}\n"
            f"Платформа: {e['platform']}\n"
            f"Ссылка: {e['profile_url']}\n"
            f"Описание: {e.get('description', '')[:300]}"
        )
    experts_text = "\n\n".join(desc)

    user_prompt = f"""
Тема мероприятия: {topic}
Сезон: {season}

Список кандидатов:
{experts_text}

Для КАЖДОГО кандидата верни JSON в одном массиве, формат:
[
  {{
    "name": "...",
    "rating": 0-10,
    "reason": "кратко, 1-2 предложения",
    "recommended": true/false
  }},
  ...
]
"""

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )

    content = resp.choices[0].message.content
    try:
        data = json.loads(content)
        if isinstance(data, list):
            return data
        return []
    except Exception:
        return []


async def analyze_speakers(topic: str, season: str, experts: List[Dict]) -> List[Dict]:
    return await asyncio.to_thread(_call_openai_sync, topic, season, experts)
