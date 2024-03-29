from __future__ import annotations

import uvicorn

from src.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)

# TODO: Перенеси инициализацию SQLAlchemy, Redis и Minio в FastAPI Lifespan Events:
#  https://fastapi.tiangolo.com/advanced/events
