from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .models import Anime, Character, Seiyu, Profile
from .service import AnimeFilter, CharacterFilter
from .serializers import (
    AnimeListSerializer,
    AnimeDetailSerializer,
    CommentCreateSerializer,
    RatingCreateSerializer,
    CharacterListSerializer,
    CharacterDetailSerializer,
    SeiyuListSerializer,
    SeiyuDetailSerializer,
    ProfileListSerializer,
    ProfileDetailSerializer,
)


class AnimeListView(generics.ListAPIView):
    queryset = Anime.objects.all().distinct()
    serializer_class = AnimeListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = AnimeFilter
    search_fields = ['title', 'description']
    ordering_fields = ['rating', 'release_date']


class AnimeDetailView(generics.RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeDetailSerializer


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CharacterFilter
    search_fields = ['name', 'description']


class CharacterDetailView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer


class SeiyuListView(generics.ListAPIView):
    queryset = Seiyu.objects.all()
    serializer_class = SeiyuListSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name', ]


class SeiyuDetailView(generics.RetrieveAPIView):
    queryset = Seiyu.objects.all()
    serializer_class = SeiyuDetailSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['user__username', ]


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer

