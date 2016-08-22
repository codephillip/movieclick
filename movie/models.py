from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200, default='Planet of the Apes')
    image = models.CharField(max_length=400, default='http://localhost/images/gridallbum3.png')
    link = models.CharField(max_length=400, default='http://localhost/downloads/movie1.zip')
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name

