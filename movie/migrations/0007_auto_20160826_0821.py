# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20160826_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(),
        ),
    ]
