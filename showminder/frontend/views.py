
import logging

from datetime import date
from imdbpie import Imdb

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from .forms import ImdbIdForm
from .models import TvShow

_log = logging.getLogger(__name__)


def imdb_titles(search):
    imdb = Imdb(anonymize=True)
    titles = []
    for item in imdb.search_for_title(search):
        print(item['title'])
        # {'imdb_id': 'tt0028599', 'title': 'Back in Circulation', 'year': '1937'},
        item['cover_url'] = imdb.get_title_by_id(item['imdb_id']).cover_url
        titles.append(item)
    return titles


class IndexView(LoginRequiredMixin, TemplateView):  # noqa
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tvshows'] = TvShow.objects.all()
        return context


class AddView(LoginRequiredMixin, FormView):  # noqa
    template_name = 'add.html'
    form_class = ImdbIdForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class DetailView(LoginRequiredMixin, TemplateView):  # noqa
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tvshow'] = get_object_or_404(TvShow, pk=kwargs['tvshow'])
        return context


class IncSeasonView(RedirectView):  # noqa
    permanent = False
    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        t = get_object_or_404(TvShow, pk=kwargs['tvshow'])
        t.season += 1
        t.episode = 1
        t.last_seen = date.today()
        t.save()
        return super().get_redirect_url(*args, **kwargs)


class IncEpisodeView(RedirectView):  # noqa
    permanent = False
    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        t = get_object_or_404(TvShow, pk=kwargs['tvshow'])
        t.episode += 1
        t.last_seen = date.today()
        t.save()
        return super().get_redirect_url(*args, **kwargs)
