from pydantic import Field

from src.settings import BaseSettings


class SQLAlchemySettings(BaseSettings):
    """Отвечает за хранение настроек, связанных с SQLAlchemy."""

    # Указывает, будет ли SQLAlchemy логировать выполняемые запросы.
    should_echo_sql: bool = Field(default=False, alias="DB_SHOULD_ECHO_SQL")

    # Добавить настройки уровня логирования логера алхимии (DEBUG, INFO, WARNING и т.д.)
