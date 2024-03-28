"""Реализует получения доступа к кэшу...

...не зависящее от конкретного провайдера (Redis, KeyDB и т.д.).
"""

from collections.abc import Awaitable

from src.cache.cache_provider import CacheProvider
from src.cache.redis_provider import RedisCacheProvider

__all__ = ["Cache", "RedisCacheProvider"]


class Cache(CacheProvider):
    """Реализация кэша с использованием одного из провайдеров."""

    _cache_provider: CacheProvider

    def __init__(self, provider: CacheProvider) -> None:
        """Устанавливает полученный cache_provider как текущую реализацию кэша."""
        super().__init__()
        self._cache_provider = provider

    async def get(self, key: bytes | str) -> Awaitable:
        """Возвращает значение из текущего провайдера."""
        return self._cache_provider.get(key)

    async def set(self, key: str, value: bytes | memoryview | str | float) -> Awaitable:
        """Устанавливает значение в текущий провайдер."""
        return self._cache_provider.set(key, value)
