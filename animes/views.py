from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Anime
from .serializers import AnimeListSerializer, AnimeDetailSerializer, CommentCreateSerializer


class AnimeListView(APIView):
    def get(self, request):
        animes = Anime.objects.all()
        serializer = AnimeListSerializer(animes, many=True)
        return Response(serializer.data)


class AnimeDetailView(APIView):
    def get(self, request, pk):
        anime = Anime.objects.get(id=pk)
        serializer = AnimeDetailSerializer(anime, many=False)
        return Response(serializer.data)


class CommentCreateView(APIView):
    def post(self, request):
        review = CommentCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response(status=201)
