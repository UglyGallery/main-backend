from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from src.models import Category, User


class Post(Base):
    """Модель поста (публикации)."""

    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    title: Mapped[str]
    description: Mapped[str | None]
    picture_link: Mapped[str]
    views: Mapped[int]
    created_at: Mapped[datetime | None]

    category: Mapped["Category"] = relationship()
    author: Mapped["User"] = relationship(back_populates="posts")
