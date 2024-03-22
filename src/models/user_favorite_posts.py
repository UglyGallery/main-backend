from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from src.models import Post, User


class UserFavoritePosts(Base):
    """Модель постов, добавленных пользователем в избранное."""

    __tablename__ = "user_favorite_posts"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), primary_key=True)

    post: Mapped["Post"] = relationship()
    user: Mapped["User"] = relationship()
