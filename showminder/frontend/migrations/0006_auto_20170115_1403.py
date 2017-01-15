# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20170115_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='cover_url',
            field=models.URLField(max_length=2023),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='trailer_url',
            field=models.URLField(max_length=2023, null=True),
        ),
    ]
