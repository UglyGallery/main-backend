from pydantic import Field
from pydantic_settings import BaseSettings


class SQLAlchemySettings(BaseSettings):
    """Хранит настройки, связанные с SQLAlchemy."""

    # Указывает, будет ли SQLAlchemy логировать выполняемые запросы.
    should_echo_sql: bool = Field(default=False, alias="DB_SHOULD_ECHO_SQL")

    # Добавить настройки уровня логирования логера алхимии (DEBUG, INFO, WARNING и т.д.)
