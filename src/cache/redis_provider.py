from typing import Any

import redis

from src.cache import CacheProvider


class RedisCacheProvider(CacheProvider):
    """Реализация кэша с использованием подключения к Redis."""

    _redis_client: redis.Redis

    def __init__(self, redis_client: redis.Redis) -> None:
        """Использует Redis для инициализации провайдера кэша."""
        super().__init__()
        self._redis_client = redis_client

    async def get(self, key: Any) -> Any | None:  # noqa: ANN401
        """Возвращает значение из Redis."""
        return self._redis_client.get(key)

    async def set(self, key: Any, value: Any) -> None:  # noqa: ANN401
        """Устанавливает значение в Redis."""
        self._redis_client.set(key, value)
