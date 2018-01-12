from django import forms

from .models import TvShow


class ImdbIdForm(forms.Form):  # noqa
    imdb_id = forms.CharField(label="Imdb ID")
    season = forms.IntegerField(initial=1, min_value=1)
    episode = forms.IntegerField(initial=1, min_value=1)

    def clean(self):
        imdb_id = self.cleaned_data['imdb_id']
        season = self.cleaned_data['season']
        episode = self.cleaned_data['episode']
        try:
            self._tvshow = TvShow.from_imdb(imdb_id, season, episode)
        except Exception as e:
            raise forms.ValidationError(f"Error! {e}")

        return imdb_id

    def save(self):
        """Import movie/show from IMDB."""
        self._tvshow.save()
