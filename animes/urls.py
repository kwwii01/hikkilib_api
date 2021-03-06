from django.urls import path
from . import views


app_name = 'anime_api'

urlpatterns = [
    path('animes/', views.AnimeListView.as_view()),
    path('animes/<int:pk>/', views.AnimeDetailView.as_view()),
    path('animes/<int:pk>/add-to-list/', views.AddUpdateDeleteAnimeInListView.as_view()),
    path('animes/<int:pk>/update-in-list/', views.AddUpdateDeleteAnimeInListView.as_view()),
    path('animes/<int:pk>/remove-from-list/', views.AddUpdateDeleteAnimeInListView.as_view()),
    path('animes/<int:pk>/check-in-list/', views.AnimeInfoFromListView.as_view()),
    path('comments/', views.CommentCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentUpdateDeleteView.as_view()),
    path('characters/', views.CharacterListView.as_view()),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view()),
    path('seiyu/', views.SeiyuListView.as_view()),
    path('seiyu/<int:pk>/', views.SeiyuDetailView.as_view()),
    path('profiles/', views.ProfileListView.as_view()),
    path('profiles/me/', views.ProfileMeView.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view()),
    path('profiles/<int:pk>/list', views.AnimeUserListView.as_view()),
    path('genres/', views.GenreListView.as_view()),
    path('statuses/', views.StatusListView.as_view()),
    path('types/', views.TypeListView.as_view()),
    path('producers/', views.ProducerListView.as_view()),
]