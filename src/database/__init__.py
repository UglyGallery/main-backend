"""Данный модуль отвечает за всё, что связано с базой данных."""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.settings import settings

pg_username = settings.postgres_username
pg_password = settings.postgres_password
pg_database = settings.postgres_database
pg_host = settings.postgres_host

connection_url = (
    f"postgresql+asyncpg://{pg_username}:{pg_password}@{pg_host}/{pg_database}"
)

async_engine = create_async_engine(
    url=connection_url,
    echo=True,
)

async_session = async_sessionmaker(async_engine)
