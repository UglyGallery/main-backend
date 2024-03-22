"""TODO: Напиши нормальный docstring."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """Возвращает сообщение "Hello World"."""
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    """Возвращает сообщение "Hello" вместе и "name"."""
    return {"message": f"Hello {name}"}
