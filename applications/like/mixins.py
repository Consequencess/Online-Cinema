from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
import logging

from applications.like import services

like_logger = logging.getLogger('LIKE')


class LikeMixin:
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        obj = self.get_object()
        user = request.user
        status_ = services.like_unlike(user=user, obj=obj)
        like_logger.info('User liked movie/User unliked movie')
        return Response({'status': status_, 'user': user.email}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def fans(self, request, pk=None):
        obj = self.get_object()
        like_logger.info('Get a list of users who have liked')
        return Response(services.get_fans(obj=obj), status=status.HTTP_200_OK)