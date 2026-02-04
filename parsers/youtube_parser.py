# parsers/youtube_parser.py

import aiohttp
from typing import List, Dict

from .keywords import TOPIC_KEYWORDS  # импорт из того же пакета


async def search_youtube_experts(
    topic: str,
    api_key: str,
    season: str | None = None,
    limit: int = 5,
) -> List[Dict]:
    url = "https://www.googleapis.com/youtube/v3/search"
    topic_lower = topic.lower()

    def build_query(include_season: bool) -> str:
        parts = [
            topic_lower,
            "тренер",
            "инструктор",
            "coach",
            "канал",
            "school",
            "academy",
            "Russia",
        ]
        for key, variants in TOPIC_KEYWORDS.items():
            if key in topic_lower:
                parts.extend(variants)
                break

        if include_season and season:
            parts.append(season)

        return " ".join(dict.fromkeys(parts))

    async def do_request(q: str) -> List[Dict]:
        params = {
            "part": "snippet",
            "q": q,
            "type": "channel",
            "order": "relevance",
            "maxResults": limit,
            "key": api_key,
            "regionCode": "RU",
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                data = await resp.json()

        experts: List[Dict] = []
        for item in data.get("items", []):
            snippet = item["snippet"]
            channel_id = item["id"]["channelId"]
            experts.append(
                {
                    "name": snippet["title"],
                    "platform": "YouTube",
                    "profile_url": f"https://www.youtube.com/channel/{channel_id}",
                    "description": snippet.get("description", ""),
                }
            )
        return experts

    # 1) пробуем без сезона
    experts = await do_request(build_query(include_season=False))
    if experts:
        return experts[:limit]

    # 2) если пусто — пробуем с сезоном
    experts = await do_request(build_query(include_season=True))
    return experts[:limit]
