
import logging

from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from .forms import ImdbIdForm
from .models import TvShow
from api.models import ApiNotification

_log = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tvshows"] = TvShow.objects.all()
        context["api_notifications"] = ApiNotification.objects.all()
        return context


class AddView(LoginRequiredMixin, FormView):
    template_name = "add.html"
    form_class = ImdbIdForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DetailView(LoginRequiredMixin, TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tvshow"] = get_object_or_404(TvShow, pk=kwargs["tvshow"])
        return context


class IncSeasonView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        t = get_object_or_404(TvShow, pk=kwargs["tvshow"])
        t.season += 1
        t.episode = 1
        t.last_seen = date.today()
        t.save()
        return super().get_redirect_url(*args, **kwargs)


class IncEpisodeView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = "/"

    def get_redirect_url(self, *args, **kwargs):
        t = get_object_or_404(TvShow, pk=kwargs["tvshow"])
        t.episode += 1
        t.last_seen = date.today()
        t.save()
        return super().get_redirect_url(*args, **kwargs)
