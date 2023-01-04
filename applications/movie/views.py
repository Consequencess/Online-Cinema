from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from applications.comments.mixins import CommentMixin
from applications.favorites.mixins import FavoriteMixin
from applications.like.mixins import LikeMixin
from applications.movie.models import Movie
from applications.movie.serializers import MovieSerializer
from applications.ratings.mixins import RatingMixin
import logging
movie_logger = logging.getLogger('MOVIE')


class MovieAPIView(RatingMixin, LikeMixin, FavoriteMixin, CommentMixin, ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    filterset_fields = ['category']
    search_fields = ['title']
    ordering_fields = ['id', 'price']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['DELETE'], detail=True)
    def del_images(self, request, pk=None):
        user = request.user
        movie = self.get_object()
        if movie.user == user:
            images = movie.images.all()
            images.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'status': 'Только владелец может удалить картинку'}, status=status.HTTP_400_BAD_REQUEST)
