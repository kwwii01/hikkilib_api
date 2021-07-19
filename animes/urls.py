from django.urls import path
from . import views


app_name = 'anime_api'

urlpatterns = [
    path('animes/', views.AnimeListView.as_view()),
    path('animes/<int:pk>', views.AnimeDetailView.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
    path('rating/', views.RatingCreateView.as_view()),
]