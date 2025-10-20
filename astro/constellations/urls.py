from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:page>/', index, name='home_page'),
    path('movies/<slug:slug>/', movie_detail, name= 'movie_detail'),
    path('genres/<int:pk>/', movies_by_genre, name = 'movies_by_genre'),
    path('genres/<int:pk>/page<int:page>/', movies_by_genre, name='movies_by_genre_page'),
    path('directors/<int:pk>/', movies_by_director, name = 'movies_by_director'),
    path('directors/<int:pk>/page<int:page>/', movies_by_director, name='movies_by_director_page'),
    path('actors/<int:pk>/', actor_detail, name = 'actor_detail'),
    path('actors/<int:pk>/page<int:page>/', actor_detail, name= 'actor_detail_page')
]