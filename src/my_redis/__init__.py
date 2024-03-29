"""Отвечает за установление соединения c Redis."""

import redis

from src.settings import settings

redis_client = redis.Redis(host=settings.redis.host, port=settings.redis.port)
