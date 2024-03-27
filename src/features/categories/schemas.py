from pydantic import BaseModel, ConfigDict


class Category(BaseModel):
    """Представляет категорию поста."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
