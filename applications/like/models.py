from django.contrib.auth import get_user_model
from django.db import models

from applications.movie.models import Movie

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='likes', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)