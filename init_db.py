# init_db.py

from database.session import engine
from database.models import Base

def main():
    Base.metadata.create_all(bind=engine)
    print("✅ DB initialized")

if __name__ == "__main__":
    main()
