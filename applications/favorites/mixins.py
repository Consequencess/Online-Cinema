from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from favorites import services


class FavoriteMixin:
    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk=None):
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
    def get_favorites(self, request):
        movie_data = services.get_favorites(user=request.user)
        return Response(movie_data, status=status.HTTP_200_OK)
