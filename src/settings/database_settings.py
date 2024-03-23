from pydantic import Field

from src.settings.base_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    """Хранит настройки, связанные с базой данных."""

    username: str = Field(alias="POSTGRES_USERNAME")
    password: str = Field(alias="POSTGRES_PASSWORD")
    host: str = Field(alias="POSTGRES_DATABASE")
    port: str = Field(alias="POSTGRES_HOST")
    database: str = Field(alias="POSTGRES_PORT")

    @property
    def url(self) -> str:
        """Возвращает url строку для соединения с базой данных."""
        url: str = f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        return url
