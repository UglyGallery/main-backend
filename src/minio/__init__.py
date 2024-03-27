"""В данном модуле находится код, связанный с файловым хранилищем MinIO."""

from minio import Minio

from src.settings import settings

minio_client = Minio(
    f"localhost:{settings.minio.port_api}",
    access_key=settings.minio.username,
    secret_key=settings.minio.password,
    secure=False,
)
