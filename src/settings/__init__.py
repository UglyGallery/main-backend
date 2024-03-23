"""Данный модуль отвечает за работу с настройками всего приложения."""

from src.settings.base_settings import BaseSettings
from src.settings.database_settings import DatabaseSettings
from src.settings.logging_settings import LoggingSettings
from src.settings.sqlalchemy_settings import SQLAlchemySettings

__all__ = [
    "BaseSettings",
    "DatabaseSettings",
    "settings",
    "SQLAlchemySettings",
    "LoggingSettings",
]


class Settings(BaseSettings):
    database: DatabaseSettings = DatabaseSettings()


settings = Settings()
