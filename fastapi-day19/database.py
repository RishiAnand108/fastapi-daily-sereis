# database.py
# Handles DB connection and session

from sqlmodel import SQLModel, create_engine, Session

# SQLite DB URL
DATABASE_URL = "sqlite:///./day19.db"

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session
