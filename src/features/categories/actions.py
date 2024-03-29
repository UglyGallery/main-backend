from pydantic import TypeAdapter
from sqlalchemy import select

from src.features.categories import schemas
from src.infrastructure.database import async_session, models


async def get_all_categories() -> list[schemas.CategoryResponse]:
    """Возвращает из базы данных список всех доступных категорий."""
    async with async_session() as session, session.begin():
        stmt = select(models.Category).order_by(models.Category.id)
        result = await session.execute(stmt)
        categories = result.scalars().all()
        return TypeAdapter(list[schemas.CategoryResponse]).validate_python(categories)
