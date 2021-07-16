from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Anime
from .serializers import AnimeListSerializer


class AnimeListView(APIView):
    def get(self, request):
        animes = Anime.objects.all()
        serializer = AnimeListSerializer(animes, many=True)
        return Response(serializer.data)


