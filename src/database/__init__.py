"""Данный модуль отвечает за всё, что связано с базой данных."""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.settings import settings

__all__ = ["get_db"]

async_engine = create_async_engine(
    url=settings.database.url,
    echo=True,
)

async_session = async_sessionmaker(async_engine)


async def get_db() -> AsyncSession:
    """Возвращает сессию для работы с базой данных.

    Данная функция используется как зависимость и может быть переопределена
    на соединение с тестовой базой данных для тестирования кода.
    """
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
