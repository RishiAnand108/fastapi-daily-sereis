from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Day 7 App"
    DEBUG: bool = True
    API_VERSION: str = 'v1'

    class Config:
        env_file = '.env'  #Load variables from .env file

settings = Settings()        