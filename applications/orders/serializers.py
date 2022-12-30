from rest_framework import serializers

from applications.movie.models import Movie
from applications.orders.tasks import send_confirm_link
from applications.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        exclude = ['confirm_code', 'order_confirm']

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.create_confirm_code()
        order.save()
        send_confirm_link.delay(order.user.email, order.confirm_code)
        return order

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        movie = Movie.objects.get(id=rep['movie']).title
        rep['order_confirm'] = instance.order_confirm
        rep['movie'] = movie
        return rep

    def validate(self, attrs):
        movie = attrs['movie']
        count = attrs['count']
        if movie.count < count:
            raise serializers.ValidationError(f'вы не можете заказать такое количество, осталось {movie.count}')
        return attrs
