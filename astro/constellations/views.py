from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from .models import Movie, Genre, Director, Actor
from .forms import ReviewForm

from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


def index(request):
    movies = Movie.objects.filter(is_published = True)
   
    context = {
        'movies': movies,
        'title': "Кинокаталог - Главная"
    }

    return render(request, 'constellations/index.html', context=context)

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    reviews = movie.reviews.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.author = request.user
                review.save()
                return redirect('movie_detail', slug=movie.slug)
        else:
            return redirect('login')
    else:
        form = ReviewForm()

    context = {
        'movie': movie,
        'reviews': reviews,
        'form': form,
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
def director_list(request):
    all_directors = Director.objects.all().order_by('last_name')
    
    paginator = Paginator(all_directors, 10) 
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'title': 'Все режиссёры'
    }
    
    return render(request, 'constellations/director_list.html', context=context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
