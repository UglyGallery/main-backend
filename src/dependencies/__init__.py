"""Реализует функции для получения распространённых зависимостей.

Например: `db: Annotated[AsyncSession, Depends(get_db)]`. Данные зависимости
являются глобальными и могут быть использована в любой фиче приложения.
"""

from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from jose import JOSEError, jwt
from minio import Minio
from sqlalchemy.ext.asyncio import AsyncSession

from src.cache import Cache, RedisCacheProvider
from src.database import async_session
from src.my_minio import minio_client
from src.my_redis import redis_client
from src.security import security, update_cached_jwt_public_key


async def get_db() -> AsyncGenerator[AsyncSession, None]:
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


async def _get_jwt_payload(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    cache: Annotated[Cache, Depends(get_cache)],
) -> dict:
    """Проверяет, если ли у пользователя доступ к запрашиваемому ресурсу."""
    token: str = credentials.credentials

    public_key: str = "apple"  # await cache.get(cache.JWT_PUBLIC_KEY)

    try:
        return jwt.decode(token, key=public_key)
    except JOSEError:
        # Если произошла ошибка, то обновляем public_key и пробуем снова.
        public_key = await update_cached_jwt_public_key(cache)
        try:
            return jwt.decode(token, key=public_key)
        except JOSEError as e:
            raise HTTPException(status_code=401, detail=str(e)) from e


async def get_filestorage() -> Minio:
    """Возвращает файловое хранилище."""
    # TODO: Сделай нормальную абстракцию, так же как для кэша.
    return minio_client


async def get_user_id(payload: Annotated[dict, Depends(_get_jwt_payload)]) -> int:
    """Возвращает ID пользователя из JWT токена.

    Предварительно проверяет токен на валидность.
    """
    return int(payload["sub"])


async def has_valid_jwt(_: Annotated[dict, Depends(_get_jwt_payload)]) -> None:
    """Проверяет, верен ли JWT токен текущего запроса."""
