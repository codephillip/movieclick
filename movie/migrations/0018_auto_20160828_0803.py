# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_auto_20160828_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
