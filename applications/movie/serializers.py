from django.db.models import Avg
from rest_framework import serializers
from applications.comments.services import is_commented
from applications.comments.models import Comment
from applications.comments.serializers import CommentSerializer
from applications.favorites.services import is_favorite
from applications.like.models import Like
from applications.like.services import is_fan
from applications.movie.models import Movie, Image
from applications.ratings.models import Rating
from applications.ratings.services import is_reviewer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        category = validated_data.pop('category')
        movie = Movie.objects.create(**validated_data)
        movie.category.set(category)
        files = request.FILES
        for image in files.getlist('images'):
            Image.objects.create(movie=movie, image=image)
        return movie

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = self.context.get('request').user
        images = []
        for i in rep['images']:
            images.append(i['image'])
        rep['images'] = images
        rep['likes'] = Like.objects.filter(movie=instance, like=True).count()
        rating = Rating.objects.filter(movie=instance).aggregate(Avg('rating'))['rating__avg']
        if rating:
            rep['rating'] = rating
        else:
            rep['rating'] = 0
        rep['is_reviewer'] = is_reviewer(user=user, obj=instance)
        rep['is_favorite'] = is_favorite(user=user, obj=instance)
        comments = Comment.objects.filter(movie=instance)
        comments = CommentSerializer(comments, many=True).data
        comments = [{'user': i['user'], 'comment': i['comment']} for i in comments]
        rep['is_commented'] = is_commented(user=user, obj=instance)
        rep['comments'] = comments
        return rep
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     user = self.context.get('request').user
    #     images = []
    #     for i in rep['images']:
    #         images.append(i['image'])
    #     rep['images'] = images
    #     rep['likes'] = Like.objects.filter(product=instance, like=True).count()
    #     rating = Rating.objects.filter(product=instance).aggregate(Avg('rating'))['rating__avg']
    #     if rating:
    #         rep['rating'] = rating
    #     else:
    #         rep['rating'] = 0
    #     comments = Comment.objects.filter(product=instance)
    #     comments = CommentSerializer(comments, many=True).data
    #     comments = [{'user': i['user'], 'comment': i['comment']} for i in comments]
    #     rep['comments'] = comments
    #     rep['is_fan'] = is_fan(user=user, obj=instance)
    #     rep['is_reviewer'] = is_reviewer(user=user, obj=instance)
    #     rep['is_commented'] = is_commented(user=user, obj=instance)
    #     rep['is_favorite'] = is_favorite(user=user, obj=instance)
    #     return