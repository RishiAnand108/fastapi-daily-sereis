from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg://fastapi_user:rishi@localhost:5432/fastapi_day8"

    class Config:
        env_file = ".env"

settings = Settings()   # <--- THIS MUST EXIST (small s)
