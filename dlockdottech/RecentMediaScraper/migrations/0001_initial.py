# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-15 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('release_date', models.DateTimeField(verbose_name='date released')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('animation_studio', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('release_date', models.DateTimeField(verbose_name='date released')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lead_actors', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('release_date', models.DateTimeField(verbose_name='date released')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lead_actors', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]