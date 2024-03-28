import abc
from collections.abc import Awaitable


class CacheProvider(abc.ABC):
    """Абстрактный класс для всех провайдеров кэша.

    Данный интерфейс описывает методы, которые должен реализовывать провайдеры
    кэша (такие, как, например, Redis).
    """

    @abc.abstractmethod
    async def get(self, key: bytes | str) -> Awaitable:
        """Возвращает значение из кэша."""

    @abc.abstractmethod
    async def set(self, key: str, value: bytes | memoryview | str | float) -> Awaitable:
        """Помещает значение в кэш."""
