from django.contrib import admin

from applications.movie.models import Category, Movie

admin.site.register(Category)
admin.site.register(Movie)
