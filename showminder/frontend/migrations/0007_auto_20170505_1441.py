# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20170115_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='last_seen',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
