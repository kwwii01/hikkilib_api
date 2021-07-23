from django.urls import path
from . import views


app_name = 'anime_api'

urlpatterns = [
    path('animes/', views.AnimeListView.as_view()),
    path('animes/<int:pk>/', views.AnimeDetailView.as_view()),
    path('comments/', views.CommentCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentUpdateDeleteView.as_view()),
    path('characters/', views.CharacterListView.as_view()),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view()),
    path('seiyu/', views.SeiyuListView.as_view()),
    path('seiyu/<int:pk>/', views.SeiyuDetailView.as_view()),
    path('profiles/', views.ProfileListView.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view()),
    path('profiles/<int:pk>/list', views.AnimeUserListView.as_view()),

]