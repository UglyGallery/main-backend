"""В данном модуле находятся модели, которые представляют таблицы в базе данных."""

from src.infrastructure.database.models.category import Category
from src.infrastructure.database.models.post import Post
from src.infrastructure.database.models.user import User
from src.infrastructure.database.models.user_favorite_posts import UserFavoritePosts
from src.infrastructure.database.models.user_profile_info import UserProfileInfo

__all__ = ["User", "UserProfileInfo", "Category", "Post", "UserFavoritePosts"]
