# database/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config.settings import Settings

settings = Settings()

engine = create_engine(settings.postgres_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Session:
    """Get database session."""
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()  # Закрытие сессии должно происходить вручную

def init_db():
    """Initialize database tables."""
    from .models import Base
    Base.metadata.create_all(bind=engine)
