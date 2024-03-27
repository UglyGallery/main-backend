from fastapi import UploadFile

from src.features.categories.schemas import CategoryResponse
from src.features.posts import schemas


async def create_new_post(
    _: schemas.PostReceive, __: UploadFile
) -> schemas.PostResponse:
    """Возвращает из базы данных список всех доступных категорий."""
    # async with async_session() as session, session.begin():
    #     stmt = select(models.Category).order_by(models.Category.id)
    #     result = await session.execute(stmt)
    #     categories = result.scalars().all()
    #     return TypeAdapter(list[schemas.Category]).validate_python(categories)

    # TODO: Допиши функцию.
    return schemas.PostResponse(
        id=1,
        category=CategoryResponse(id=1, name=""),
        title="",
        picture_link="",
        views=1,
    )
