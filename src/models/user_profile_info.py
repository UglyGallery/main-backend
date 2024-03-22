from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from src.models import User


class UserProfileInfo(Base):
    """Модель с информацией из профиля пользователя."""

    __tablename__ = "user_profile_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    profile_picture_link: Mapped[str]
    about: Mapped[str]
    website_link: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="user_info")
