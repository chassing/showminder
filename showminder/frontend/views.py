import logging
from datetime import date

from api.models import ApiNotification
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView

from .models import TvShow

_log = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = TvShow
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        if title := self.request.GET.get("search"):
            return TvShow.objects.filter(title__icontains=title)
        else:
            query = TvShow.objects.all()
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if search := self.request.GET.get("search"):
            context["search"] = f"search={search}"

        if not context.get("is_paginated", False):
            return context

        paginator = context.get("paginator")
        num_pages = paginator.num_pages
        current_page = context.get("page_obj")
        page_no = current_page.number

        if num_pages <= 10 or page_no <= 6:  # case 1 and 2
            pages = [x for x in range(1, min(num_pages + 1, 11))]
        elif page_no > num_pages - 6:  # case 4
            pages = [x for x in range(num_pages - 9, num_pages + 1)]
        else:  # case 3
            pages = [x for x in range(page_no - 5, page_no + 5)]

        context.update({"pages": pages})
        return context


class DetailView(LoginRequiredMixin, TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tvshow"] = get_object_or_404(TvShow, pk=kwargs["tvshow"])
        return context


class AddView(LoginRequiredMixin, TemplateView):
    template_name = "add.html"


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


@login_required
def search_tmdb(request):
    tv_shows = []
    if query := request.POST.get("search"):
        tv_shows = TvShow.search(query=query)
    context = {"results": tv_shows}
    return render(request, "partials/search-results.html", context)


class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


@login_required
def add_tv(request, tmdb_id):
    TvShow.create(tmdb_id=tmdb_id)
    return HTTPResponseHXRedirect(redirect_to="/")
