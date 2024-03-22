from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Отвечает за хранение конфигурационных настроек приложения."""

    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    postgres_username: str
    postgres_password: str
    postgres_database: str
    postgres_host: str
    postgres_port: str


settings = Settings()
