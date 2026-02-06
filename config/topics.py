# config/topics.py

KANT_TOPICS = {
    "winter": {
        "label": "Зимний сезон в КАНТ",
        "topics": ["горные лыжи", "сноуборд", "беговые лыжи"],
        "default": "горные лыжи",
    },
    "spring": {
        "label": "Весенний сезон в КАНТ",
        "topics": ["трейлраннинг", "шоссе", "походы"],
        "default": "трейлраннинг",
    },
    "summer": {
        "label": "Летний сезон в КАНТ",
        "topics": ["трейлраннинг", "велосипед", "походы", "триатлон"],
        "default": "триатлон",
    },
    "autumn": {
        "label": "Осенний сезон в КАНТ",
        "topics": ["трейлраннинг", "велосипед", "походы"],
        "default": "трейлраннинг",
    },

    "run": {
        "keywords": ["бег", "running", "марафон", "забег", "темп", "пульс"],
        "skills_file": "run-speakers.md"
    },
    "xc-ski": {
        "keywords": ["беговые лыжи", "лыжи", "skiing", "коньковый", "классический"],
        "skills_file": "xc-ski-speakers.md"
    },
    "snowboard": {
        "keywords": ["сноуборд", "snowboard", "фристайл", "карвинг"],
        "skills_file": "snowboard-speakers.md"
    },
    "alpine": {
        "keywords": ["горные лыжи", "alpine", "слалом", "спуск"],
        "skills_file": "alpine-speakers.md"
    },
    "cycling": {
        "keywords": ["велоспорт", "cycling", "велосипед", "шоссе", "мтб"],
        "skills_file": "cycling-speakers.md"
    },
    "hiking": {
        "keywords": ["поход", "hiking", "треккинг", "горы"],
        "skills_file": "hiking-speakers.md"
    },
    "swim": {
        "keywords": ["плавание", "swimming", "бассейн", "кроль"],
        "skills_file": "swim-speakers.md"
    },
    "trailrun": {
        "keywords": ["трейл", "trail", "бег по горам", "ультра"],
        "skills_file": "trailrun-speakers.md"
    },
}
