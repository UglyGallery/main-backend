from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.features import categories, posts

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Инициализирует общие ресурсы, такие как соединение с БД или Redis."""
    yield


app = FastAPI(lifespan=lifespan)

origins = ["*"]

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categories.router)
app.include_router(posts.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)

# TODO: Перенеси инициализацию SQLAlchemy, Redis и Minio в FastAPI Lifespan Events:
#  https://fastapi.tiangolo.com/advanced/events
