from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Anime, Character, Seiyu
from .serializers import (
    AnimeListSerializer,
    AnimeDetailSerializer,
    CommentCreateSerializer,
    RatingCreateSerializer,
    CharacterListSerializer,
    CharacterDetailSerializer,
    SeiyuListSerializer,
    SeiyuDetailSerializer,
)


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
    permission_classes = [IsAuthenticated]

    def post(self, request):
        comment = CommentCreateSerializer(data=request.data, context={'user': request.user})
        if comment.is_valid():
            comment.save()
        return Response(comment.data)


class RatingCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        rating = RatingCreateSerializer(data=request.data, context={'user': request.user})
        if rating.is_valid():
            rating.save()
        return Response(rating.data)


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer


class CharacterDetailView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer


class SeiyuListView(generics.ListAPIView):
    queryset = Seiyu.objects.all()
    serializer_class = SeiyuListSerializer


class SeiyuDetailView(generics.RetrieveAPIView):
    queryset = Seiyu.objects.all()
    serializer_class = SeiyuDetailSerializer
