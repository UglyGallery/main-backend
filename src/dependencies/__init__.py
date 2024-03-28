"""Реализует функции для получения распространённых зависимостей.

Например: `db: Annotated[AsyncSession, Depends(get_db)]`
"""

from minio import Minio
from sqlalchemy.ext.asyncio import AsyncSession

from src.cache import Cache, RedisCacheProvider
from src.database import async_session
from src.minio import minio_client
from src.redis import redis_client


async def get_db() -> AsyncSession:
    """Возвращает сессию для работы с базой данных."""
    db = async_session()
    try:
        yield db
    finally:
        await db.close()


async def get_cache() -> Cache:
    """Возвращает кэш."""
    redis_provider = RedisCacheProvider(redis_client)
    return Cache(redis_provider)


async def get_filestorage() -> Minio:
    """Возвращает файловое хранилище."""
    # TODO: Сделай нормальную абстракцию, так же как для кэша.
    return minio_client
