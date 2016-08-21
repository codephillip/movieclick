from django.shortcuts import render

from movie.models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {
        'movies': movies
    })


def download(request, pk):
    return render(request, 'download.html', {
        'pk': pk
    })
