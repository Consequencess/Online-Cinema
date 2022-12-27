from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer


def add_del_favorite(obj, user):
    """
    Добавляет/Удаляет фильм из избранных
    :param obj:
    :param user:
    :return:
    """
    fav_obj, is_created = Favorite.objects.get_or_create(movie=obj, user=user)
    fav_obj.is_favorite = not fav_obj.is_favorite
    fav_obj.save()
    if fav_obj.is_favorite:
        return 'Добавлено в избранные'
    return 'Удалено из избранных'


def is_favorite(obj, user):
    """
    Проверяет находится ли фильм в избранных у пользователя
    :param obj:
    :param user:
    :return:
    """
    try:
        return Favorite.objects.filter(movie=obj, user=user, is_favorite=True).exists()
    except TypeError:
        return False


def get_favorites(user):
    """
    выводит список избранных фильма
    :param user:
    :return:
    """
    try:
        movie = Favorite.objects.filter(user=user, is_favorite=True)
        serializer = FavoriteSerializer(movie, many=True)
        return serializer.data
    except TypeError:
        return []