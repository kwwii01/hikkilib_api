from rest_framework import serializers

from .models import Anime


class AnimeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('title', 'type', 'year')
