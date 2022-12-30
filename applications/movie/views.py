from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from applications.favorites.mixins import FavoriteMixin
from applications.like.mixins import LikeMixin
from applications.movie.models import Movie
from applications.movie.serializers import MovieSerializer
from applications.ratings.mixins import RatingMixin


class MovieAPIView(RatingMixin, LikeMixin, FavoriteMixin, ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
