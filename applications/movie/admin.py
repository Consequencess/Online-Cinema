from django.contrib import admin

from applications.movie.models import Category, Movie

admin.site.register(Movie)
admin.site.register(Category)
