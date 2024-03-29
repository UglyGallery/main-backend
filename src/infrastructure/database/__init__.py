"""Данный модуль отвечает за всё, что связано с базой данных."""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.settings import settings

__all__ = ["async_session"]

async_engine = create_async_engine(
    url=settings.database.url,
    echo=True,
)

async_session = async_sessionmaker(async_engine)
