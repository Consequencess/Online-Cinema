from django.db.models import Avg
from rest_framework import serializers

from applications.favorites.services import is_favorite
from applications.like.models import Like
from applications.movie.models import Movie
from applications.ratings.models import Rating
from applications.ratings.services import is_reviewer


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        category = validated_data.pop('category')
        movie = Movie.objects.create(**validated_data)
        movie.category.set(category)
        return movie

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = self.context.get('request').user
        rep['likes'] = Like.objects.filter(movie=instance, like=True).count()
        rating = Rating.objects.filter(movie=instance).aggregate(Avg('rating'))['rating__avg']
        if rating:
            rep['rating'] = rating
        else:
            rep['rating'] = 0
        rep['is_reviewer'] = is_reviewer(user=user, obj=instance)
        rep['is_favorite'] = is_favorite(user=user, obj=instance)
        return rep