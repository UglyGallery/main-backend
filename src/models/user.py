from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from src.models import UserFavoritePosts, UserProfileInfo


class User(Base):
    """Модель пользователя."""

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]
    nickname: Mapped[str]
    created_at: Mapped[datetime | None]

    user_info: Mapped["UserProfileInfo"] = relationship(back_populates="user")
    favorite_posts: Mapped[list["UserFavoritePosts"]] = relationship()
