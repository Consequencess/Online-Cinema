from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorites')
    is_favorite = models.BooleanField(default=False)
