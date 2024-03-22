from __future__ import annotations

import asyncio

from src.database import async_engine
from src.database.models.base import Base


async def async_main() -> None:
    """Стартовая точка всего приложения."""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(async_main())
