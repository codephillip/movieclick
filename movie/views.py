from django.shortcuts import render
from movie.models import Category, Movie
from django.utils.encoding import smart_str
from datetime import date

import simplejson as json
import urllib2

next_limit = 60
varx = "hello"


def index(request):
    print('index')
    categorys = Category.objects.all()
    # get the latest year to display on the index page
    index_page_category = Category.objects.all().order_by('-year')
    first_id = index_page_category[0].id
    # pass the current category to the browse page
    category_browse = Category.objects.get(id=first_id)
    movies = Movie.objects.filter(category=Category.objects.filter(id=first_id)).order_by('-popularity')[:12]
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
        movies = Movie.objects.filter(category=category_browse).order_by('-popularity')[:12]
        next_limit = 60
    elif end == 60:
        movies = Movie.objects.filter(category=category_browse).order_by('-popularity')[next_limit: next_limit + 12]
        next_limit += 12
    else:
        movies = Movie.objects.filter(category=category_browse).order_by('-popularity')[pk: end + 12]
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
            movies = Movie.objects.all().order_by('-popularity')
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


# development purposes only
def update_db(request):
    item = connect_to_server()
    return render(request, 'updatedb.html', {
        'item': item
    })


def connect_to_server():
    for page in range(1, 11):
        for year in get_years():
            print('PAGE' + str(page))
            base_url = "http://api.themoviedb.org/3/discover/movie?primary_release_year=" + \
                       str(year) + "&sort_by=popularity.desc&api_key=ae6766bd4f9bebf18e24c1bc0c2c282a&"
            actual_url = base_url + "page=" + str(page)
            # actual_url = 'http://localhost/downloads/movie1.json'
            print('actual: ' + actual_url)
            json_string = json.load(urllib2.urlopen(actual_url))

            print(json_string.get('results'))
            results = json_string.get('results')
            print(results)

            for x in results:
                global varx
                varx = smart_str(x.get('original_title'))

                try:
                    if x.get('poster_path'):
                        image = 'http://image.tmdb.org/t/p/w300' + x.get('poster_path')
                    else:
                        image = 'http://image.tmdb.org/t/p/w300/zrAO2OOa6s6dQMQ7zsUbDyIBrAP.jpg'
                    save_to_db(smart_str(x.get('original_title')), image,
                               smart_str(x.get('overview')), x.get('popularity'), x.get('vote_average'),
                               x.get('release_date'), year)
                except Exception:
                    print(str(Exception))
                    continue
    return varx


def get_years():
    years = []
    year = date.today().year
    for x in range(1, 5):
        years.append(year)
        year -= 1
    return years


def save_to_db(title, image, overview, popularity, vote_average, release_date, year):
    try:
        cate_object = Category.objects.get(year=year)
    except Exception:
        # incase category doesnt exist, create it
        cate_object = Category(year=year).save()
    movie = Movie(name=title, image=image, category=cate_object, description=overview, vote_average=vote_average,
                  popularity=popularity,
                  release_date=release_date)
    movie.save()


def remove_adblocker(request):
    return render(request, 'remove_adblocker.html')
