from rest_framework import serializers

from applications.like.models import Like
from applications.movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        category = validated_data.pop('category')
        movie = Movie.objects.create(**validated_data)
        movie.category.set(category)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = self.context.get('request').user
        # rep['status'] = instance.status
        rep['likes'] = Like.objects.filter(movie=instance, like=True).count()
        return rep
