from django.urls import path

from . import views

app_name = "frontend"
urlpatterns = [
    path(r"inc-season/<int:tvshow>/", views.IncSeasonView.as_view(), name="inc-season"),
    path(r"inc-episode/<int:tvshow>/", views.IncEpisodeView.as_view(), name="inc-episode"),
    path(r"detail/<tvshow>/", views.DetailView.as_view(), name="detail"),
    path(r"add/", views.AddView.as_view(), name="add"),
    path(r"", views.IndexView.as_view(), name="index"),
]

htmx_urlpatterns = [
    path("_search/", views.search_tmdb, name="htmx-search-tmdb"),
    path("_add/<int:tmdb_id>/", views.add_tv, name="htmx-add-tv"),
]
urlpatterns += htmx_urlpatterns
