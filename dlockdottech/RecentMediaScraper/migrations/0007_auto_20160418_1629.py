# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-18 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecentMediaScraper', '0006_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='TMDB_size',
        ),
        migrations.AddField(
            model_name='config',
            name='TMDB_JSON_size',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AddField(
            model_name='config',
            name='TMDB_secureBaseurl',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
