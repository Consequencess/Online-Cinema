from django.contrib import admin

from applications.movie.models import Category, Movie, Image

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Image)
