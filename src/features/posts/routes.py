from typing import Annotated

from fastapi import APIRouter, Depends

from src.features.posts.actions import create_new_post

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/")
async def create_new_post_route(
    new_post_id: Annotated[int, Depends(create_new_post)],
) -> int:
    """Создаёт новый пост."""
    return new_post_id


# @router.put("/image")
# async def add_image_to_post(
#     post_id: int,
#     new_post: Annotated[schemas.PostResponse, Depends(create_new_post)],
# ) -> schemas.PostResponse:
#     """Добавляет в пост изображение и делаем его видимым."""
#     return new_post
