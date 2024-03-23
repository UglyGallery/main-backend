from pathlib import Path

from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticBaseSettings):
    """Базовый класс для всех настроек.

    Также отвечает за чтение значений из .env файла.
    """

    model_config = SettingsConfigDict(
        env_file=Path("../../.env"), env_file_encoding="utf-8"
    )
