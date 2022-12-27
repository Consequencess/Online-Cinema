from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from applications.like import mixins
from applications.movie.models import Movie
from applications.movie.permission import IsAdmin
from applications.movie.serializers import MovieSerializer


class MovieAPIView(mixins.LikeMixin,  ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
