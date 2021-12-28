from datetime import date

import tmdbsimple as tmdb
from django.conf import settings
from django.db import models

tmdb.REQUESTS_TIMEOUT = 5
tmdb.API_KEY = settings.TMDB_API_KEY


def unix0():
    return date.fromtimestamp(0)


class TvShow(models.Model):
    """TV Show (Movie or Series)."""

    # todo
    # alternative namen!
    # refresh from db in detail view
    # link zur admin seite in detail view
    # löschen button
    title = models.CharField(max_length=255)
    tmdb_id = models.CharField(max_length=20, null=True)
    cover_url = models.URLField(max_length=2023)
    rating = models.FloatField()
    genres = models.CharField(max_length=255, null=True, blank=True)
    tagline = models.TextField(default="No tagline.", blank=True)
    release_date = models.DateField(null=True)
    typ = models.CharField(default="tv_series", max_length=30)
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
            cover_url=settings.TMDB_BASE_URL + tv.poster_path if tv.poster_path else "",
            rating=tv.vote_average,
            tagline=tv.overview,
            release_date=tv.first_air_date,
            genres=", ".join([g["name"] for g in tv.genres]),
            typ="tv",
            last_seen=date.today(),
        )

    @classmethod
    def search(cls, query):
        search = tmdb.Search()
        search.tv(query=query, include_adult=True)
        return [
            cls(
                title=s["name"],
                tmdb_id=s["id"],
                cover_url=settings.TMDB_BASE_URL + s["poster_path"] if s["poster_path"] else "",
                rating=s["vote_average"],
                tagline=s["overview"],
                release_date=s.get("first_air_date"),
                typ="tv",
            )
            for s in search.results
        ]
