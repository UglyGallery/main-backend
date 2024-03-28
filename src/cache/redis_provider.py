from collections.abc import Awaitable

import aioredis

from src.cache import CacheProvider


class RedisCacheProvider(CacheProvider):
    """Реализация кэша с использованием подключения к Redis."""

    _redis_client: aioredis.Redis

    def __init__(self, redis: aioredis.Redis) -> None:
        """Использует Redis для инициализации провайдера кэша."""
        super().__init__()
        self.redis_client = redis

    async def get(self, key: bytes | str) -> Awaitable:
        """Возвращает значение из Redis."""
        return self.redis_client.get(key)

    async def set(self, key: str, value: bytes | memoryview | str | float) -> Awaitable:
        """Устанавливает значение в Redis."""
        return self.redis_client.set(key, value)
