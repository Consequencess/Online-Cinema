from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.comments import services
import logging

comment_logger = logging.getLogger('COMMENT')


class CommentMixin:
    @action(methods=['POST'], detail=True)
    def give_comment(self, request, pk=None):
        try:
            comment = request.data['comment']
            user = request.user
            obj = self.get_object()
            status_ = services.give_comment(user=user, obj=obj, comment=comment)
            comment_logger.info('User give comment')
            return Response(
                {
                    'status': status_,
                    'user': user.email,
                    'comment': comment
                }, status=status.HTTP_200_OK
            )
        except MultiValueDictKeyError:
            return Response('поле comment обьязательно')

    @action(methods=['POST'], detail=True)
    def del_comment(self, request, pk=None):
        user = request.user
        obj = self.get_object()
        services.del_comment(obj=obj, user=user)
        comment_logger.info('User deleted comment')
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=True)
    def commentators(self, request, pk=None):
        return Response(services.get_commentators(obj=self.get_object()), status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def comments(self, request):
        comment_logger.info('User got a list of comments')
        return Response(services.get_comments(user=request.user), status=status.HTTP_200_OK)

