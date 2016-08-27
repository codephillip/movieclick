from django.shortcuts import render
from movie.models import Category, Movie
import simplejson as json
import urllib2

next_limit = 60
varx = "hello"


def index(request):
    print('index')
    categorys = Category.objects.all()
    category_browse = Category.objects.get(id=1)
    movies = Movie.objects.filter(category=Category.objects.filter(id=1))[:12]
    return render(request, 'index.html', {
        'movies': movies,
        'categorys': categorys,
        'category_browse': category_browse
    })


def browse(request, pk, year):
    global next_limit
    end = int(pk)
    categorys = Category.objects.all()
    category_browse = Category.objects.get(year=year)
    if end == 1:
        movies = Movie.objects.filter(category=category_browse)[:12]
        next_limit = 60
    elif end == 60:
        movies = Movie.objects.filter(category=category_browse)[next_limit: next_limit + 12]
        next_limit += 12
    else:
        movies = Movie.objects.filter(category=category_browse)[pk: end + 12]
    return render(request, 'index.html', {
        'movies': movies,
        'categorys': categorys,
        'category_browse': category_browse
    })


def download(request, pk):
    movie = Movie.objects.get(pk=pk)
    categorys = Category.objects.all()
    return render(request, 'download.html', {
        'pk': pk,
        'movie': movie,
        'categorys': categorys
    })


def search(request):
    print('post result' + request.POST['movie'])
    categorys = Category.objects.all()

    if request.POST:
        if request.POST['movie'] == 'Search:':
            movies = Movie.objects.all()
        else:
            movies = Movie.objects.filter(name__contains=request.POST['movie'])
    else:
        movies = Movie.objects.all()[:12]
    return render(request, 'search.html', {
        'movies': movies,
        'categorys': categorys
    })


def watch(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'watch.html', {
        'pk': pk,
        'movie': movie
    })


def connect_to_server():
    for page in range(1, 11):
        # if page <= 24:
        #     continue
        print('PAGE' + str(page))
        base_url = "http://api.themoviedb.org/3/discover/movie?primary_release_year=2014&sort_by=popularity.desc&api_key=ae6766bd4f9bebf18e24c1bc0c2c282a&"
        actual_url = base_url + 'page=' + str(page)
        # actual_url = 'http://localhost/downloads/movie1.json'
        print('actual: ' + actual_url)
        result = json.load(urllib2.urlopen(actual_url))

        print(result.get('results'))
        result2 = result.get('results')
        print(result2)

        for x in result2:
            global varx
            print(x.get('original_title'))
            print(x.get('poster_path'))
            print(x.get('overview'))
            varx = x.get('original_title')

            try:
                save_to_db(x.get('original_title'), 'http://image.tmdb.org/t/p/w300' + x.get('poster_path'),
                           x.get('overview'), x.get('vote_average'), x.get('release_date'))
            except Exception:
                print(str(Exception))
                save_to_db(x.get('original_title'), x.get('poster_path'),
                           x.get('overview'), x.get('vote_average'), x.get('release_date'))
    return varx


def save_to_db(title, image, overview, vote_average, release_date):
    cate_object = Category.objects.get(year='2014')
    movie = Movie(name=title, image=image, category=cate_object, description=overview, vote_average=vote_average,
                  release_date=release_date)
    movie.save()


# this is for development purposes only
def updatedb(request):
    item = connect_to_server()
    return render(request, 'updatedb.html', {
        'item': item
    })


def remove_adblocker(request):
    return render(request, 'remove_adblocker.html')
