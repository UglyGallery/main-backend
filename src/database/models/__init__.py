"""В данном модуле находятся модели, которые представляют таблицы в базе данных."""

from src.database.models.category import Category
from src.database.models.post import Post
from src.database.models.user import User
from src.database.models.user_favorite_posts import UserFavoritePosts
from src.database.models.user_profile_info import UserProfileInfo

__all__ = ["User", "UserProfileInfo", "Category", "Post", "UserFavoritePosts"]
