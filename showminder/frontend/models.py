from django.db import models
from imdbpie import Imdb

imdb = Imdb(anonymize=True)


class TvShow(models.Model):
    """TV Show."""

    title = models.TextField()
    cover_url = models.URLField()
    rating = models.FloatField()
    season = models.IntegerField(default=1)
    episode = models.IntegerField(default=1)

    class Meta:  # noqa
        ordering = ['title']

    def __str__(self):  # noqa
        return self.title

    @classmethod
    def from_imdb(cls, imdb_id):
        item = imdb.get_title_by_id(imdb_id)
        tvshow = cls(title=item.title, cover_url=item.cover_url, rating=item.rating)
        return tvshow
