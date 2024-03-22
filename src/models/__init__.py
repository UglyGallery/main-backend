"""В данном модуле находятся модели, которые представляют таблицы в базе данных."""

from src.models.category import Category
from src.models.post import Post
from src.models.user import User
from src.models.user_favorite_posts import UserFavoritePosts
from src.models.user_profile_info import UserProfileInfo

__all__ = ["User", "UserProfileInfo", "Category", "Post", "UserFavoritePosts"]
