# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-08 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecentMediaScraper', '0004_auto_20160408_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='original_language',
            field=models.CharField(default=' ', max_length=3),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(default=' ', verbose_name='overview'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(default=' ', verbose_name='date released'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]