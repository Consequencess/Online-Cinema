from rest_framework import serializers


class FavoriteSerializer(serializers.Serializer):
    movie = serializers.CharField()