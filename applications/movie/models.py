from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models



User = get_user_model()


class Category(models.Model):
    title = models.SlugField(max_length=30, primary_key=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Movie(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

