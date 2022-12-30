from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ManyToManyField(Category, related_name='movie')
    user = models.ForeignKey(User, related_name='movies', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.title


