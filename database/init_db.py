import os
import sys

# Путь к корню проекта (папка выше database)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from database.session import init_db  # импорт после добавления PROJECT_ROOT

if __name__ == "__main__":
    init_db()
    print("✅ База данных готова!")
