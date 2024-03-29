import datetime
import logging
import uuid
from typing import Annotated

from fastapi import Depends, File, HTTPException, UploadFile, status
from minio import Minio
from minio.error import MinioException
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src import dependencies
from src.database import models
from src.features.posts import schemas


async def create_new(
    post_info: schemas.PostReceive,
    db: Annotated[AsyncSession, Depends(dependencies.get_db)],
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


async def add_image(
    post_id: int,
    # TODO: Ограничь, какие типы файлов разрешены.
    post_image: Annotated[UploadFile, File(description="Изображение в посте")],
    db: Annotated[AsyncSession, Depends(dependencies.get_db)],
    fs: Annotated[Minio, Depends(dependencies.get_filestorage)],
) -> None:
    """Добавляет к посту изображение."""
    try:
        # TODO: Hardcoded строка. Поменяй.
        # fs.make_bucket("avatars")
        file_name = str(uuid.uuid4()) + ".png"
        fs.put_object("avatars", file_name, post_image.file, post_image.size)
    except MinioException as e:
        # TODO: Добавь *НОРМАЛЬНОЕ* логирование. И пиши логи на русском.
        logging.exception("MinIO failed:")
        raise HTTPException(
            status_code=500, detail="Не получилось загрузить изображение"
        ) from e

    async with db as session, session.begin():
        # TODO: Поднимает ошибку, если пост не найден. Обработай ошибку.
        post: models.Post = (
            await session.scalars(select(models.Post).where(models.Post.id == post_id))
        ).one()

        post.picture_link = f"avatars/{file_name}"
        post.visible = True


async def make_visible(
    post_id: int,
    db: Annotated[AsyncSession, Depends(dependencies.get_db)],
    user_id: Annotated[int, Depends(dependencies.get_user_id)],
) -> None:
    """Делает пост видимым.

    Пост разрешает сделать видимым, если:
    1. У поста присутствует изображение.
    2. Запрос отправлен автором поста.
    """
    async with db as session, session.begin():
        try:
            post: models.Post = (
                await session.scalars(
                    select(models.Post).where(
                        models.Post.id == post_id and models.Post.author_id == user_id
                    )
                )
            ).one()
        except NoResultFound as err:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Указанный пост не найден.",
            ) from err

        if not post.picture_link:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="У поста отсутствует изображение.",
            )

        post.visible = True


async def get_post_by_id(
    post_id: int,
    db: Annotated[AsyncSession, Depends(dependencies.get_db)],
) -> schemas.PostResponse:
    """Возвращает пост по указанному ID."""
    async with db as session, session.begin():
        try:
            post: models.Post = (
                await session.scalars(
                    select(models.Post)
                    .where(models.Post.id == post_id)
                    .options(selectinload(models.Post.category))
                )
            ).one()
        except NoResultFound as err:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Указанный пост не найден.",
            ) from err
        else:
            return schemas.PostResponse.model_validate(post)
