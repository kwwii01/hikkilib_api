from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, filters

from django_filters.rest_framework import DjangoFilterBackend

from .models import Anime, Character, Seiyu, Profile, Comment, AnimeList, AnimeListItem
from .permissions import IsCommentOwnerOrAdmin
from .service import AnimeFilter, CharacterFilter
from .serializers import (
    AnimeListSerializer,
    AnimeDetailSerializer,
    CommentCreateSerializer,
    CharacterListSerializer,
    CharacterDetailSerializer,
    SeiyuListSerializer,
    SeiyuDetailSerializer,
    ProfileListSerializer,
    ProfileDetailSerializer,
    AnimeUserListSerializer,
    AnimeListItemSerializer,
    AnimeListItemMinSerializer,
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


class CommentUpdateDeleteView(APIView):
    permission_classes = [IsCommentOwnerOrAdmin]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        self.check_object_permissions(request, comment)
        serializer = CommentCreateSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class AnimeUserListView(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        anime_list = profile.anime_list
        serializer = AnimeUserListSerializer(anime_list, many=False)
        return Response(serializer.data)


class AddUpdateAnimeInListView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Anime.objects.get(pk=pk)
        except Anime.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        anime = self.get_object(pk)
        serializer = AnimeListItemSerializer(data=request.data, context={'user': request.user,
                                                                         'anime': anime})
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        anime = self.get_object(pk)
        try:
            current_user = request.user
            current_profile = Profile.objects.get(user=current_user)
            item = current_profile.anime_list.items.get(anime=anime)
            serializer = AnimeListItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except [AnimeListItem.DoesNotExist, Profile.DoesNotExist]:
            raise Http404


class AnimeInfoFromListView(APIView):
    def get_current_profile(self, request):
        try:
            current_profile = Profile.objects.get(user=request.user)
            return current_profile
        except Profile.DoesNotExist:
            raise Http404

    def get_searched_anime(self, pk):
        try:
            anime = Anime.objects.get(pk=pk)
            return anime
        except Anime.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        if request.user.is_authenticated:
            current_profile = self.get_current_profile(request)
            anime = self.get_searched_anime(pk)
            try:
                item = current_profile.anime_list.items.get(anime=anime)
                serializer = AnimeListItemMinSerializer(item, many=False)
                return Response(serializer.data)
            except AnimeListItem.DoesNotExist:
                return JsonResponse({'message': 'Anime is not in list'}, safe=False)
        else:
            return JsonResponse({'message': 'User is not authenticated'}, safe=False)
