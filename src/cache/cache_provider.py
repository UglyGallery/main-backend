import abc
from typing import Any


class CacheProvider(abc.ABC):
    """Абстрактный класс для всех провайдеров кэша.

    Данный интерфейс описывает методы, которые должен реализовывать провайдеры
    кэша (такие, как, например, Redis).
    """

    @abc.abstractmethod
    async def get(self, key: Any) -> Any | None:  # noqa: ANN401
        """Возвращает значение из кэша."""

    @abc.abstractmethod
    async def set(self, key: Any, value: Any) -> None:  # noqa: ANN401
        """Помещает значение в кэш."""
