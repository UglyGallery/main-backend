from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.database.models import Category, User


class Post(Base):
    """Модель поста (публикации)."""

    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    title: Mapped[str]
    description: Mapped[str | None]
    picture_link: Mapped[str | None]
    views: Mapped[int] = mapped_column(default=0)
    visible: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    category: Mapped["Category"] = relationship(back_populates="posts")
    author: Mapped["User"] = relationship(back_populates="posts")
