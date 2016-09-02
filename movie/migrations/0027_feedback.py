# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0026_movie_trailer_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, null=True, unique=True)),
                ('date', models.DateField(max_length=100, null=True)),
            ],
        ),
    ]