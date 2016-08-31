from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_str, force_unicode


class Category(models.Model):
    year = models.IntegerField(default=2016)

    def __unicode__(self):
        return str(self.year)


class Movie(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    image = models.CharField(max_length=250, default='http://image.tmdb.org/t/p/w300/zrAO2OOa6s6dQMQ7zsUbDyIBrAP.jpg',
                             null=True)
    download_link = models.CharField(max_length=400, default='http://www.movieclick.xyz/movie_not_found', null=True)
    watch_link = models.CharField(max_length=400,
                                  default='http://www.movieclick.xyz/movie_not_found',
                                  null=True)
    description = models.TextField(null=True)
    release_date = models.CharField(max_length=100, null=True)
    vote_average = models.CharField(max_length=100, null=True)
    popularity = models.FloatField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    genre_pk = models.IntegerField(unique=True, null=True)

    def __unicode__(self):
        return self.name


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie)
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return force_unicode(smart_str((self.movie.name))) + " # " + force_unicode(smart_str((self.genre.name)))
