"""Отвечает за установление соединения c Redis."""

import aioredis

from src.settings import settings

redis_client = aioredis.Redis(host=settings.redis.host, port=settings.redis.port)
