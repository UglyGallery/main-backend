from typing import Annotated

from fastapi import APIRouter, Depends

from src import dependencies
from src.features.posts import actions, schemas

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/")
async def create_new_route(
    new_post_id: Annotated[int, Depends(actions.create_new)],
) -> int:
    """Создаёт новый пост."""
    # TODO: Возвращай Pydantic модель, а не примитив.
    return new_post_id


@router.put(
    "/image",
    status_code=201,
    dependencies=[Depends(dependencies.get_user_id), Depends(actions.add_image)],
)
async def add_image_route() -> None:
    """Добавляет в пост изображение и делаем его видимым."""


@router.get("/make-visible", dependencies=[Depends(actions.make_visible)])
async def make_visible_route() -> None:
    """Добавляет в пост изображение и делаем его видимым."""


@router.get(
    "/{post_id}",
    dependencies=[Depends(dependencies.has_valid_jwt)],
    response_model=schemas.PostResponse,
)
async def get_post_by_id_route(
    post: Annotated[schemas.PostResponse, Depends(actions.get_post_by_id)],
) -> schemas.PostResponse:
    """Создаёт новый пост."""
    return post
