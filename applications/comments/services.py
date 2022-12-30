from applications.comments.models import Comment
from applications.comments.serializers import CommentSerializer


def give_comment(obj, user, comment):
    """
    Пользователь оставляет комментарии
    :param obj:
    :param user:
    :param comment:
    :return:
    """
    comment_obj, is_created = Comment.objects.get_or_create(user=user, movie=obj)
    comment_obj.comment = comment
    comment_obj.save()
    if is_created:
        return 'Комментарий создан!'
    return 'Комментарий обнавлен!'


def del_comment(obj, user):
    try:
        Comment.objects.get(movie=obj, user=user).delete()
    except Comment.DoesNotExist:
        pass


def is_commented(obj, user):
    try:
        return Comment.objects.filter(user=user, movie=obj).exists()
    except TypeError:
        return False


def get_commentators(obj):
    """
    Выводит список комментаторов и комментариев к продукту
    :param obj:
    :return:
    """
    commentators = Comment.objects.filter(movie=obj)
    serializer = CommentSerializer(commentators, many=True)
    commentators = [{'user': i['user'], 'comment': i['comment']} for i in serializer.data]
    return commentators


def get_comments(user):
    """
    Выводит список комментариев пользователя
    :param user:
    :return:
    """
    comments = Comment.objects.filter(user=user)
    serializer = CommentSerializer(comments, many=True)
    comments = [{'movie': i['movie'], 'comment': i['comment']} for i in serializer.data]
    return comments