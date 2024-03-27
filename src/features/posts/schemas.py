from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.features.categories.schemas import CategoryReceive, CategoryResponse


class PostReceive(BaseModel):
    """Представляет данные о посте, которые ожидаются на вход."""

    title: str
    description: str | None
    category: CategoryReceive


class PostResponse(BaseModel):
    """Представляет данные о посте, которые будут возвращены."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    category: CategoryResponse
    title: str
    description: str | None = None
    picture_link: str
    views: int
    created_at: datetime | None = None  # TODO: Убери None. И в ORM модели Alchemy тоже.