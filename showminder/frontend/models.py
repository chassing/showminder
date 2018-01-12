
from datetime import date
from datetime import datetime
from django.db import models
from imdbpie import Imdb

imdb = Imdb()


def unix0():
    return date.fromtimestamp(0)


class TvShow(models.Model):
    """TV Show (Movie or Series)."""

    title = models.CharField(max_length=255)
    imdb_id = models.CharField(max_length=20, null=True)
    cover_url = models.URLField(max_length=2023)
    trailer_url = models.URLField(max_length=2023, null=True)
    rating = models.FloatField()
    genres = models.CharField(max_length=255, null=True)
    tagline = models.TextField(default="No tagline.", blank=True)
    release_date = models.DateField(null=True)
    typ = models.CharField(default='tv_series', max_length=30)
    # my attributes
    last_seen = models.DateTimeField(auto_now=True)
    season = models.IntegerField(default=1)
    episode = models.IntegerField(default=1)

    class Meta:  # noqa
        ordering = ['-last_seen', 'title']

    def __str__(self):  # noqa
        return self.title

    @classmethod
    def from_imdb(cls, imdb_id, season=0, episode=0):
        item = imdb.get_title(imdb_id)
        try:
            release_date = datetime.strptime(item.release_date, '%Y-%m-%d').date()
        except:
            release_date = unix0()

        title = item['base']['title']

        try:
            cover_url = item['base']['image']['url']
        except KeyError:
            cover_url = ""
        try:
            rating = item['ratings']['rating']
        except KeyError:
            rating = 0
        try:
            tagline = item['plot']['summaries'][0]['text']
        except KeyError:
            tagline = ""
        try:
            typ = item['base']['titleType']
        except KeyError:
            typ = ""

        tvshow = cls(
            title=title,
            imdb_id=imdb_id,
            cover_url=cover_url,
            # trailer_url=item.trailers[0]['url'] if item.trailers else None,
            trailer_url=None,
            rating=rating,
            # genres=", ".join(item.genres),
            genres="",
            tagline=tagline,
            release_date=release_date,
            typ=typ,
            last_seen=date.today(),
            season=season,
            episode=episode,
        )
        return tvshow
