from pathlib import Path

from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticBaseSettings):
    """Отвечает за чтение настроек из .env файла."""

    model_config = SettingsConfigDict(
        env_file=Path("../../.env"), env_file_encoding="utf-8"
    )
