from pydantic import BaseModel, ConfigDict


class CategoryReceive(BaseModel):
    """Представляет категорию поста, которая ожидается на вход."""

    name: str


class CategoryResponse(BaseModel):
    """Представляет категорию поста, которая будет возвращена."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
