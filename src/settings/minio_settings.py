from pydantic import Field
from pydantic_settings import BaseSettings


class MinIOSettings(BaseSettings):
    """Хранит настройки, связанные с файловым хранилищем MinIO."""

    username: str = Field(alias="MINIO_ROOT_USER")
    password: str = Field(alias="MINIO_ROOT_PASSWORD")
    volume: str = Field(alias="MINIO_VOLUMES")
    port_api: str = Field(alias="MINIO_PORT_API")
    port_console: str = Field(alias="MINIO_PORT_CONSOLE")
