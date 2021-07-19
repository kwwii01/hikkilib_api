from rest_framework import serializers

from .models import Anime, Comment, Rating, AnimeScreenshots


class AnimeListSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Anime
        fields = ('title', 'type', 'year')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('anime', 'text')

    def create(self, validated_data):
        comment = Comment(
            text=validated_data['text'],
            user=self.context.get('user'),
            anime=validated_data['anime'],
        )
        comment.save()
        return comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'text', 'publish_date')


class AnimeScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeScreenshots
        fields = ('screenshot', )


class AnimeDetailSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    producer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    characters = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)
    comments = CommentSerializer(many=True)
    anime_screenshots = AnimeScreenshotSerializer(many=True)

    class Meta:
        model = Anime
        fields = '__all__'


class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('anime', 'score')

    def create(self, validated_data):
        chosen_anime = validated_data['anime']
        current_user = self.context.get('user')
        score = validated_data['score']
        rating = Rating.objects.filter(anime=chosen_anime, user=current_user)
        if not rating:
            rating = Rating(
                anime=chosen_anime,
                score=score,
                user=current_user,
            )
        else:
            rating = Rating.objects.get(anime=chosen_anime, user=current_user)
            rating.score = score
        rating.save()
        return rating
