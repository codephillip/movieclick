# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0024_auto_20160831_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='notfoundmovie',
            name='release_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
