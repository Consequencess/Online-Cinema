from rest_framework import serializers


class FanSerializer(serializers.Serializer):
    user = serializers.CharField(required=True)