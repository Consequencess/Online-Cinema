from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.favorites import services
import logging

favorite_logger = logging.getLogger('FAVORITE')


class FavoriteMixin:
    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk=None):
        favorite_logger.info('User added to favorites/User removed from favorites')
        obj = self.get_object()
        user = request.user
        status_ = services.add_del_favorite(user=user, obj=obj)
        return Response(
            {
                'status': status_,
                'user': user.email,
                'movie': obj.title
            },
            status=status.HTTP_200_OK
        )

    @action(methods=['GET'], detail=True)
    def get_favorites(self, request, pk=None):
        favorite_logger.info('The user gets a list of their favorites')
        movie_data = services.get_favorites(user=request.user)
        return Response(movie_data, status=status.HTTP_200_OK)
