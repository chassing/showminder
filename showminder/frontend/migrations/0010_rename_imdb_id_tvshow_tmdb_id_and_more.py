# Generated by Django 4.0 on 2021-12-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20180422_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tvshow',
            old_name='imdb_id',
            new_name='tmdb_id',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='trailer_url',
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]