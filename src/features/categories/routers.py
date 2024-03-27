from fastapi import APIRouter

from src.features.categories import schemas
from src.features.categories.actions import get_all_categories

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/")
async def get_categories() -> list[schemas.CategoryResponse]:
    """Возвращает список всех доступных категорий."""
    return await get_all_categories()
