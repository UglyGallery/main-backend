from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from src.settings.database_settings import DatabaseSettings
from src.settings.logging_settings import LoggingSettings
from src.settings.minio_settings import MinIOSettings
from src.settings.redis_settings import RedisSettings
from src.settings.sqlalchemy_settings import SQLAlchemySettings

load_dotenv()


class Settings(BaseSettings):
    """Хранит все настройки приложения."""

    database: DatabaseSettings = DatabaseSettings()
    logging: LoggingSettings = LoggingSettings()
    sqlalchemy: SQLAlchemySettings = SQLAlchemySettings()
    minio: MinIOSettings = MinIOSettings()
    redis: RedisSettings = RedisSettings()


settings = Settings()
