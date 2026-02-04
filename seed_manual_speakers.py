# seed_manual_speakers.py

from database.session import SessionLocal
from database.models import ManualSpeaker

# Список ручных спикеров — пример, потом подставишь свои каналы
SEED_SPEAKERS = [
    # ТРИАТЛОН
    {
        "name": "Triathlon Russia Channel",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@triathlon_russia",
        "description": "Канал о тренировках и стартах по триатлону в России.",
        "season": "summer",
        "topic": "триатлон",
        "region": "Россия",
    },
    {
        "name": "Ural Triathlon Club",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@ural_tri_club",
        "description": "Клуб триатлона в УрФО, разбор тренировок и стартов.",
        "season": "summer",
        "topic": "триатлон",
        "region": "УрФО",
    },

    # ТРЕЙЛРАННИНГ
    {
        "name": "Ural Trail Running",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@ural_trail_running",
        "description": "Трейлы и горные забеги на Урале, советы по подготовке.",
        "season": "spring",
        "topic": "трейлраннинг",
        "region": "УрФО",
    },
    {
        "name": "Russian Trail Running",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@russian_trail",
        "description": "Трейлраннинг по всей России, обзоры стартов и экипировки.",
        "season": "autumn",
        "topic": "трейлраннинг",
        "region": "Россия",
    },

    # ПОХОДЫ / ТУРИЗМ
    {
        "name": "Походы по Уралу",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@ural_hiking",
        "description": "Маршруты и советы по походам в Уральском регионе.",
        "season": "summer",
        "topic": "походы",
        "region": "УрФО",
    },
    {
        "name": "Russian Hiking Guide",
        "platform": "YouTube",
        "profile_url": "https://www.youtube.com/@russian_hiking",
        "description": "Пеший туризм, трекинг и снаряжение для походов по России.",
        "season": "autumn",
        "topic": "походы",
        "region": "Россия",
    },
]


def main():
    db = SessionLocal()
    try:
        for data in SEED_SPEAKERS:
            # Проверяем, нет ли уже такого URL в базе
            exists = (
                db.query(ManualSpeaker)
                .filter(ManualSpeaker.profile_url == data["profile_url"])
                .first()
            )
            if exists:
                continue

            speaker = ManualSpeaker(**data)
            db.add(speaker)

        db.commit()
        print("✅ Manual speakers seeded.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
