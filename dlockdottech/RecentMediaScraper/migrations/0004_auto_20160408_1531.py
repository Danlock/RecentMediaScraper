# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-08 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecentMediaScraper', '0003_auto_20160408_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='vote_average',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
