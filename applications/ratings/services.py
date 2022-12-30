from applications.like import serializers
from applications.ratings.models import Rating
from applications.ratings.serializers import ReviewerSerializer


def give_rating(obj, user, rating):
    """
    Ставит рейтинг
    :param obj:
    :param user:
    :param rating:
    :return:
    """
    if 0 <= int(rating) <= 5:
        rating_obj, is_created = Rating.objects.get_or_create(user=user, movie=obj)
        rating_obj.rating = rating
        rating_obj.save()
        if not is_created:
            return 'Рейтинг обновлен!'
        return 'Рейтинг создан!'
    raise serializers.ValidationError('Неверно введен рейтинг')


def del_rating(obj, user):
    """
    Удаляет рейтинг
    :param obj:
    :param user:
    :return:
    """
    try:
        Rating.objects.get(movie=obj, user=user).delete()
    except Rating.DoesNotExist:
        pass


def is_reviewer(obj, user):
    """
    Оставлял ли пользователь рейтинг
    :param obj:
    :param user:
    :return:
    """
    try:
        return Rating.objects.filter(user=user, movie=obj).exists()
    except TypeError:
        return False


def get_reviewers(obj):
    users = Rating.objects.filter(movie=obj)
    serializer = ReviewerSerializer(users, many=True)
    return serializer.data