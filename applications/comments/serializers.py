from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    user = serializers.EmailField()
    comment = serializers.CharField()
    movie = serializers.CharField()