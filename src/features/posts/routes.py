from fastapi import APIRouter, UploadFile

from src.features.posts import schemas
from src.features.posts.actions import create_new_post

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/")
async def create_new(
    post: schemas.PostReceive, image: UploadFile
) -> schemas.PostResponse:
    """Создаёт новый пост."""
    return await create_new_post(post, image)
