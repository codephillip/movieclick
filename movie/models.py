from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=400)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name

