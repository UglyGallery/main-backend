"""Реализует получения доступа к кэшу...

...не зависящее от конкретного провайдера (Redis, KeyDB и т.д.).
"""

from typing import Any

from src.cache.cache_provider import CacheProvider
from src.cache.redis_provider import RedisCacheProvider

__all__ = ["Cache", "CacheProvider", "RedisCacheProvider"]


class Cache(CacheProvider):
    """Реализация кэша с использованием одного из провайдеров."""

    JWT_PUBLIC_KEY = "jwt-public-key"

    _cache_provider: CacheProvider

    def __init__(self, provider: CacheProvider) -> None:
        """Устанавливает полученный cache_provider как текущую реализацию кэша."""
        super().__init__()
        self._cache_provider = provider

    async def get(self, key: Any) -> Any | None:  # noqa: ANN401
        """Возвращает значение из текущего провайдера."""
        return await self._cache_provider.get(key)

    async def set(self, key: Any, value: Any) -> None:  # noqa: ANN401
        """Устанавливает значение в текущий провайдер."""
        await self._cache_provider.set(key, value)
