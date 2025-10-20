from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from .models import Movie, Genre, Director, Actor

def index(request):
    movies = Movie.objects.filter(is_published = True)

    paginator = Paginator(movies, 4)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        # 'movie_list': movies,
        'page_obj': page_obj,
        'title': "Кинокаталог - Главная"
    }

    return render(request, 'constellations/index.html', context=context)

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    context = {
        'movie': movie,
        'title': f'Фильм {movie.title}'
    }

    return render(request, 'constellations/movie_detail.html', context=context)


def movies_by_genre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    movies = genre.movies.filter(is_published=True)

    paginator = Paginator(movies, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        # 'movies_list': movies,
        'page_obj': page_obj,
        'title': f'Фильмы в жанре: {genre.name}'
    }
    return render(request, 'constellations/movie_list.html', context=context)

def movies_by_director(request, pk):
    director = get_object_or_404(Director, pk=pk) 
    movies = director.movies.filter(is_published=True)  

    paginator = Paginator(movies, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': f'Фильмы режиссёра: {director}'  
    }
    return render(request, 'constellations/movie_list.html', context=context)


def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    movies = actor.movies.filter(is_published = True)

    paginator = Paginator(movies, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'actor': actor,
        # 'movies_list': movies,
        'page_obj': page_obj,
        'title': f'Информация об актёре: {actor}'
    }

    return render(request, 'constellations/actor_detail.html', context=context)