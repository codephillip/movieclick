from django.shortcuts import render

from movie.models import Movie

next_limit = 60


def index(request):
    movies = Movie.objects.all()[:12]
    return render(request, 'index.html', {
        'movies': movies
    })


def browse(request, pk):
    global next_limit
    end = int(pk)
    if end == 1:
        movies = Movie.objects.all()[:12]
        next_limit = 60
    elif end == 60:
        movies = Movie.objects.all()[next_limit: next_limit + 12]
        next_limit += 12
    else:
        movies = Movie.objects.all()[pk: end + 12]
    return render(request, 'index.html', {
        'movies': movies
    })


def download(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'download.html', {
        'pk': pk,
        'movie': movie
    })
