from django.urls import path

from . import views

app_name = "frontend"
urlpatterns = [
    path(r"inc-season/<int:tvshow>/", views.inc_season_view, name="inc-season"),
    path(r"inc-episode/<int:tvshow>/", views.inc_episode_view, name="inc-episode"),
    path(r"delete/<int:tvshow>/", views.delete_view, name="delete"),
    path(r"detail/<int:tvshow>/", views.detail_view, name="detail"),
    path(r"add/", views.add_view, name="add"),
    path(r"", views.IndexView.as_view(), name="index"),
]

htmx_urlpatterns = [
    path("_search_for_add/", views.htmx_search_tmdb_for_add, name="htmx-search-tmdb-for-add"),
    path("_search_for_refresh/<int:tvshow>/", views.htmx_search_tmdb_for_refresh, name="htmx-search-tmdb-for-refresh"),
    path("_add/<int:tmdb_id>/", views.htmx_add_tv, name="htmx-add-tv"),
    path("_refresh/<int:tvshow>/<int:tmdb_id>/", views.htmx_refresh_tv, name="htmx-refresh-tv"),
]
urlpatterns += htmx_urlpatterns
