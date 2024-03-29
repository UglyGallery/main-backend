import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src import dependencies
from src.database import models
from src.features.posts import schemas


async def create_new_post(
    # TODO: Ограничь, какие типы файлов разрешены.
    # post_image: Annotated[UploadFile, File(description="A file read as UploadFile")],
    post_info: schemas.PostReceive,
    db: Annotated[AsyncSession, Depends(dependencies.get_db)],
    # fs: Annotated[Minio, Depends(dependencies.get_filestorage)],
    user_id: Annotated[int, Depends(dependencies.get_user_id)],
) -> int:
    """Создаёт новый пост."""
    async with db as session, session.begin():
        # TODO: Поднимает ошибку, если пользователь не найден. Но искать пользователя
        #  лучше в зависимости dependencies.get_user_id, которая лучше должна
        #  возвращать не ID, а сразу модель из БД. И там же поднимать ошибку,
        #  если пользователь не найден.

        # TODO: Обработай ошибку.
        category: models.Category = (
            await session.scalars(
                select(models.Category).where(
                    models.Category.name == post_info.category.name
                )
            )
        ).one()

        post: models.Post = models.Post(
            author_id=user_id,
            category=category,
            title=post_info.title,
            description=post_info.description,
            visible=False,
            created_at=datetime.datetime.now(datetime.UTC),
        )

        session.add(post)
        await session.flush()
        return post.id

    # try:
    #     # TODO: Hardcoded строка. Поменяй.
    #     fs.make_bucket("avatars")
    #     fs.put_object(
    #         "avatars", str(uuid.uuid4()), post_image.file, post_image.size
    #     )
    # except MinioException as e:
    #     # TODO: Добавь *НОРМАЛЬНОЕ* логирование. И пиши логи на русском.
    #     logging.exception("MinIO failed:")
    #     await session.rollback()
    #     raise HTTPException(
    #         status_code=500, detail="Couldn't create a post. Try again later"
    #     ) from e
    # else:
