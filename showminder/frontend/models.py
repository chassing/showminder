from datetime import date

import tmdbsimple as tmdb
from django.conf import settings
from django.db import models
from django.templatetags.static import static

tmdb.REQUESTS_TIMEOUT = 5
tmdb.API_KEY = settings.TMDB_API_KEY


def unix0():
    return date.fromtimestamp(0)


def poster_url(poster_path):
    if poster_path:
        return settings.TMDB_BASE_URL + poster_path
    return static("images/image-placeholder-500x500.jpg")


class TvShow(models.Model):
    """TV Show (Movie or Series)."""

    # todo
    # alternative namen!
    # löschen button
    title = models.CharField(max_length=255)
    tmdb_id = models.CharField(max_length=20, null=True)
    cover_url = models.URLField(max_length=2023)
    rating = models.FloatField()
    genres = models.CharField(max_length=255, null=True, blank=True)
    tagline = models.TextField(default="No tagline.", blank=True)
    release_date = models.DateField(null=True)
    typ = models.CharField(default="tv_series", max_length=30)
    movie_db = models.CharField(default="imdb", max_length=30)
    # my attributes
    last_seen = models.DateTimeField(auto_now=True)
    season = models.IntegerField(default=1)
    episode = models.IntegerField(default=1)

    class Meta:  # noqa
        ordering = ["-last_seen", "title"]

    def __str__(self):  # noqa
        return self.title

    @classmethod
    def create(cls, tmdb_id):
        tv = tmdb.TV(tmdb_id)
        tv.info()
        return cls.objects.create(
            title=tv.name,
            tmdb_id=tv.id,
            cover_url=poster_url(tv.poster_path),
            rating=tv.vote_average,
            tagline=tv.overview,
            release_date=date.fromisoformat(tv.first_air_date) if tv.first_air_date else unix0(),
            genres=", ".join([g["name"] for g in tv.genres]),
            typ="tv",
            last_seen=date.today(),
            movie_db="tmdb",
        )

    @classmethod
    def search(cls, query):
        search = tmdb.Search()
        search.tv(query=query, include_adult=True)
        return sorted(
            [
                cls(
                    title=s["name"],
                    tmdb_id=s["id"],
                    cover_url=poster_url(s["poster_path"]),
                    rating=s["vote_average"],
                    tagline=s["overview"],
                    release_date=date.fromisoformat(s.get("first_air_date")) if s.get("first_air_date") else unix0(),
                )
                for s in search.results
            ],
            key=lambda x: x.release_date,
            reverse=True,
        )

    def refresh_from_tmdb(self, tmdb_id):
        tv = tmdb.TV(tmdb_id)
        tv.info()
        self.title = tv.name
        self.tmdb_id = tv.id
        self.movie_db = "tmdb"
        self.cover_url = poster_url(tv.poster_path)
        self.rating = tv.vote_average
        self.tagline = tv.overview
        self.release_date = date.fromisoformat(tv.first_air_date) if tv.first_air_date else unix0()
        self.genres = ", ".join([g["name"] for g in tv.genres])
        self.typ = "tv"
        self.save()
