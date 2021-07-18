from rest_framework import serializers

from .models import Anime, Comment


class AnimeListSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Anime
        fields = ('title', 'type', 'year')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'text')

class AnimeDetailSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    producer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    characters = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)
    comments = CommentCreateSerializer(many=True)

    class Meta:
        model = Anime
        fields = '__all__'
