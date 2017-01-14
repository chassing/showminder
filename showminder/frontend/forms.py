from django import forms

from .models import TvShow


class ImdbIdForm(forms.Form):  # noqa
    imdb_id = forms.CharField(label="Imdb ID", help_text="adfadf")

    def clean_imdb_id(self):
        imdb_id = self.cleaned_data['imdb_id']
        try:
            self._tvshow = TvShow.from_imdb(imdb_id)
        except:
            raise forms.ValidationError("Imdb ID not found!")

        return imdb_id

    def save(self):
        """Import movie/show from IMDB."""
        self._tvshow.save()
