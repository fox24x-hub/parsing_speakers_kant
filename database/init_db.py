import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.sql import text
from config.settings import settings

async def init_db():
    engine = create_async_engine(settings.postgres_url, echo=True)
    
    async with engine.connect() as conn:
        # Создаём таблицу speakers
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS speakers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                platform VARCHAR(50),
                profile_url VARCHAR(500),
                contacts TEXT,
                audience_size INTEGER,
                rating FLOAT DEFAULT 0.0,
                season VARCHAR(20),
                topic VARCHAR(100),
                kant_category VARCHAR(100),
                gpt_analysis TEXT,
                is_contacted BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
            );
        """))
        
        # Индексы
        await conn.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_speakers_season_rating ON speakers(season, rating DESC);
        """))
        
        await conn.commit()
    
    print("✅ База данных готова!")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())
