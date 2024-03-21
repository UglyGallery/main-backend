import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

# TODO: Напоминание себе: "Напиши нормальный compose.yml,
#  а не используй этот костыль. Глупенький".
load_dotenv()

pg_username = os.environ.get("POSTGRES_USERNAME")
pg_password = os.environ.get("POSTGRES_PASSWORD")
pg_database = os.environ.get("POSTGRES_DATABASE")
pg_host = os.environ.get("POSTGRES_HOST")

async_engine = create_async_engine(
    url=f"postgresql+asyncpg://{pg_username}:{pg_password}@{pg_host}/{pg_database}",
    echo=True,
)

async_session = async_sessionmaker(async_engine)
