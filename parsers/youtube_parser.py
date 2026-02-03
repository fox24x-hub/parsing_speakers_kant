import aiohttp
from typing import List, Dict

async def search_youtube_experts(topic: str, api_key: str, limit: int = 5) -> List[Dict]:
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": f"{topic} горные лыжи тренер инструктор",
        "type": "channel",
        "order": "relevance",
        "maxResults": limit,
        "key": api_key,
        "regionCode": "RU",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            data = await resp.json()

    experts = []
    for item in data.get("items", []):
        snippet = item["snippet"]
        channel_id = item["id"]["channelId"]
        experts.append({
            "name": snippet["title"],
            "platform": "YouTube",
            "profile_url": f"https://www.youtube.com/channel/{channel_id}",
            "description": snippet.get("description", ""),
        })

    return experts
