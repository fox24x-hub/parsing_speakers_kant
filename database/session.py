# database/session.py (пример)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base  # важно, чтобы здесь уже были Speaker и ManualSpeaker

engine = create_engine("sqlite:///speakers.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
