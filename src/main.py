"""Hello, World!"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Возвращает сообщение "Hello World"."""
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """Возвращает сообщение "Hello" вместе и "name"."""
    return {"message": f"Hello {name}"}
