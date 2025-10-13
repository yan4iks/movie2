from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('movies/<slug:slug>/', movie_detail, name= 'movie_detail'),
    path('genres/<int:pk>/', movies_by_genre, name = 'movies_by_genre'),
    path('directors/<int:pk>/', movies_by_director, name = 'movies_by_director')
]