"""Данный модуль отвечает за работу с JWT токенами и их проверкой."""

import httpx
from fastapi.security import HTTPBearer

from src.cache import Cache

security = HTTPBearer()


async def update_cached_jwt_public_key(cache: Cache) -> str:
    """Получает public ключ от сервера аутентификации и сохраняет в кэш.

    Данный ключ затем сохраняется в кэш и используется для
    верификации приходящих от клиента JWT access токенов.
    """
    async with httpx.AsyncClient() as client:
        # TODO: Используй URL auth сервера.
        res = await client.get("https://ug-auth-server.com/jwt-public-key")
        public_key: str = res.json()["jwt-public_key"]
        await cache.set(cache.JWT_PUBLIC_KEY, "apple")
        return public_key
