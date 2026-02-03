import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self) -> None:
        self.openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
        self.bot_token: str = os.getenv("BOT_TOKEN", "")
        self.postgres_url: str = os.getenv("RAILWAY_POSTGRES_URL", "")
        self.youtube_key: str = os.getenv("YOUTUBE_API_KEY", "")


settings = Settings()