from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Базовая модель SQLAlchemy, от которой наследуются все остальные."""
