from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Speaker(Base):
    __tablename__ = "speakers"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    platform = Column(String(50))
    profile_url = Column(String(500))
    description = Column(Text)
    rating = Column(Float, default=0.0)
    recommended = Column(Boolean, default=False)
    season = Column(String(20))
    topic = Column(String(100))
    gpt_reason = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
class ManualSpeaker(Base):
    __tablename__ = "manual_speakers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    platform = Column(String, nullable=False, default="RuTube")  # RuTube, VK, YouTube и т.п.
    profile_url = Column(String, nullable=False)
    description = Column(Text, default="")
    season = Column(String, nullable=True)   # winter/spring/summer/autumn
    topic = Column(String, nullable=True)    # "триатлон", "трейлраннинг" и т.д.
    region = Column(String, nullable=True)   # например, "УрФО"
    active = Column(Boolean, default=True)