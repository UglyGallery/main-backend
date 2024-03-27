from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from src.settings.database_settings import DatabaseSettings
from src.settings.logging_settings import LoggingSettings
from src.settings.sqlalchemy_settings import SQLAlchemySettings

load_dotenv()


class Settings(BaseSettings):
    """Хранит все настройки приложения."""

    database: DatabaseSettings = DatabaseSettings()
    logging: LoggingSettings = LoggingSettings()
    sqlalchemy: SQLAlchemySettings = SQLAlchemySettings()


settings = Settings()
