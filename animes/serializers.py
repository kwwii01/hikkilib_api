from rest_framework import serializers

from .models import Anime, Comment, AnimeScreenshots, Character, Seiyu, Profile, AnimeList, AnimeListItem


class AnimeListSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Anime
        fields = ('id', 'title', 'poster', 'type', 'year', 'status', 'rating')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('anime', 'text')

    def create(self, validated_data):
        profile = Profile.objects.get(user=self.context.get('user'))
        comment = Comment(
            text=validated_data['text'],
            profile=profile,
            anime=validated_data['anime'],
        )
        comment.save()
        return comment


class ProfileListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'picture')


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer(read_only=True, many=False)

    class Meta:
        model = Comment
        fields = ('id', 'profile', 'text', 'publish_date')


class AnimeScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeScreenshots
        fields = ('screenshot', )


class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name', 'picture', 'main_character')


class AnimeDetailSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    producer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    characters = CharacterListSerializer(read_only=True, many=True)
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)
    comments = CommentSerializer(many=True)
    anime_screenshots = AnimeScreenshotSerializer(many=True)

    class Meta:
        model = Anime
        fields = '__all__'


class SeiyuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seiyu
        fields = ('id', 'name', 'picture')


class CharacterDetailSerializer(serializers.ModelSerializer):
    related_animes = AnimeListSerializer(read_only=True, many=True)
    seiyu = SeiyuListSerializer(read_only=True, many=False)

    class Meta:
        model = Character
        fields = '__all__'


class SeiyuDetailSerializer(serializers.ModelSerializer):
    voiced_characters = CharacterListSerializer(read_only=True, many=True)

    class Meta:
        model = Seiyu
        fields = '__all__'


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    anime_list = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class AnimeListItemMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeListItem
        exclude = ('list', 'anime', 'id')


class AnimeListItemSerializer(serializers.ModelSerializer):
    anime = AnimeListSerializer(many=False, read_only=True)

    class Meta:
        model = AnimeListItem
        exclude = ('list', )

    def create(self, validated_data):
        chosen_anime = self.context.get('anime')
        current_user = self.context.get('user')
        profile = Profile.objects.get(user=current_user)
        anime_list = AnimeList.objects.get(profile=profile)
        score = None
        status = None
        try:
            score = validated_data['score']
            status = validated_data['status']
        except KeyError:
            score = AnimeListItem.DO_NOT_MATCH
            status = 'Planned'

        try:
            item = anime_list.items.get(anime=chosen_anime)
            return item
        except AnimeListItem.DoesNotExist:
            item = anime_list.items.create(anime=chosen_anime, score=score, status=status)
            return item


class AnimeUserListSerializer(serializers.ModelSerializer):
    items = AnimeListItemSerializer(many=True)
    profile = ProfileListSerializer(many=False)

    class Meta:
        model = AnimeList
        fields = '__all__'
