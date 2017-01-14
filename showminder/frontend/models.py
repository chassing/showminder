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
    last_seen = models.DateField()

    class Meta:  # noqa
        ordering = ['-last_seen', 'title']

    def __str__(self):  # noqa
        return self.title

    @classmethod
    def from_imdb(cls, imdb_id, season, episode, last_seen):
        item = imdb.get_title_by_id(imdb_id)
        tvshow = cls(
            title=item.title,
            cover_url=item.cover_url,
            rating=item.rating,
            season=season,
            episode=episode,
            last_seen=last_seen,
        )
        return tvshow
