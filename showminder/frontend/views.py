import logging
from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.list import ListView

from .models import TvShow

_log = logging.getLogger(__name__)


class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


class IndexView(LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = TvShow
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        if title := self.request.GET.get("search"):
            return TvShow.objects.filter(title__icontains=title)
        else:
            query = TvShow.objects.all()
        return query

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return ["partials/series-list.html"]
        return super().get_template_names()

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


@login_required
def detail_view(request, tvshow):
    return render(
        request, "detail.html", {"tvshow": get_object_or_404(TvShow, pk=tvshow)}
    )


@login_required
def add_view(request):
    return render(request, "add.html", {})


@login_required
def inc_season_view(request, tvshow):
    t = get_object_or_404(TvShow, pk=tvshow)
    t.season += 1
    t.episode = 1
    t.last_seen = date.today()
    t.save()
    return redirect("frontend:index")


@login_required
def inc_episode_view(request, tvshow):
    t = get_object_or_404(TvShow, pk=tvshow)
    t.episode += 1
    t.last_seen = date.today()
    t.save()
    return redirect("frontend:index")


@login_required
def delete_view(request, tvshow):
    t = get_object_or_404(TvShow, pk=tvshow)
    t.delete()
    return redirect("frontend:index")


@login_required
def htmx_search_tmdb_for_add(request):
    return _htmx_search_tmdb(request, "partials/search-results.html", {})


@login_required
def htmx_search_tmdb_for_refresh(request, tvshow):
    return _htmx_search_tmdb(
        request, "partials/refresh-results.html", {"tvshow": tvshow}
    )


def _htmx_search_tmdb(request, template, context):
    tv_shows = []
    if query := request.POST.get("search"):
        tv_shows = TvShow.search(query=query)
    context["results"] = tv_shows

    return render(request, template, context)


@login_required
def htmx_add_tv(request, tmdb_id):
    TvShow.create(tmdb_id=tmdb_id)
    return HTTPResponseHXRedirect(redirect_to="/")


@login_required
def htmx_refresh_tv(request, tvshow, tmdb_id):
    t = get_object_or_404(TvShow, pk=tvshow)
    t.refresh_from_tmdb(tmdb_id)
    return HTTPResponseHXRedirect(
        redirect_to=reverse("frontend:detail", kwargs={"tvshow": tvshow})
    )
