from django.contrib.auth import get_user_model
from django.db import models


from applications.movie.models import Movie


User = get_user_model()


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')

