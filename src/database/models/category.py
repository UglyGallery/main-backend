from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.database.models import Post


class Category(Base):
    """Модель категории поста (публикации)."""

    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    posts: Mapped[list["Post"]] = relationship()
