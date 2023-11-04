import os

from pathlib import Path

from functools import lru_cache

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file=os.path.join(BASE_DIR, '.env'),
        env_file_encoding='utf-8'
    )


class MongoSettings(Settings):
    MONGO_INITDB_DATABASE: str
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_HOST: str
    MONGO_INITDB_PORT: str

    @property
    def mongo_settings(self) -> dict:
        return {
            'user': self.MONGO_INITDB_ROOT_USERNAME,
            'password': self.MONGO_INITDB_ROOT_PASSWORD,
            'host': self.MONGO_INITDB_HOST,
            'port': self.MONGO_INITDB_PORT,
            'database': self.MONGO_INITDB_DATABASE
        }

    @property
    def get_uri(self) -> str:
        return 'mongodb://{user}:{password}@{host}:{port}/{database}'.format(**self.mongo_settings)


class DefaultSettings(Settings):
    DIR: str = str(BASE_DIR)
    DEBUG: bool
    TELEGRAM_TOKEN: str
    MONGO: MongoSettings = MongoSettings()


@lru_cache()
def get_default_settings() -> DefaultSettings:
    return DefaultSettings()
