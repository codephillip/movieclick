from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    year = models.IntegerField(default=2016)

    def __unicode__(self):
        return str(self.year)


class Movie(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    image = models.CharField(max_length=250, default='http://image.tmdb.org/t/p/w300/zrAO2OOa6s6dQMQ7zsUbDyIBrAP.jpg', null=True)
    download_link = models.CharField(max_length=400, default='http://localhost/downloads/movie1.zip', null=True)
    watch_link = models.CharField(max_length=400, default='http://dl.fardadownload.ir/Film/2016/Suicide.Squad.2016.%20English.CAM.FardaDownload.mp4', null=True)
    description = models.TextField(null=True)
    release_date = models.CharField(max_length=100, null=True)
    vote_average = models.CharField(max_length=100, null=True)
    popularity = models.FloatField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
