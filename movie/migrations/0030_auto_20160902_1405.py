# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0029_auto_20160902_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(null=True),
        ),
    ]