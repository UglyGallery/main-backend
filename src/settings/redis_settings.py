from pydantic import Field
from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    """Хранит настройки, связанные с файловым хранилищем MinIO."""

    port: int = Field(alias="REDIS_PORT")
    password: str = Field(alias="REDIS_PASSWORD")
    host: str = Field(alias="REDIS_HOST")
