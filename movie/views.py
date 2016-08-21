from django.shortcuts import render

from movie.models import Movie


def index(request):
    movies = Movie.objects.all()[:12]
    return render(request, 'index.html', {
        'movies': movies
    })


def download(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'download.html', {
        'pk': pk,
        'movie': movie
    })
