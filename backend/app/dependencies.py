from functools import lru_cache

from pydantic_settings import BaseSettings
from sqlmodel import create_engine


class Settings(BaseSettings):
    DATABASE_URL: str

    ui_url: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()

engine = create_engine(settings.DATABASE_URL)
