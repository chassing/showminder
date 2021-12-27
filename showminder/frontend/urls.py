from django.urls import path

from .views import AddView, DetailView, IncEpisodeView, IncSeasonView, IndexView

app_name = "frontend"
urlpatterns = [
    path(r"inc-season/<tvshow>/", IncSeasonView.as_view(), name="inc-season"),
    path(r"inc-episode/<tvshow>/", IncEpisodeView.as_view(), name="inc-episode"),
    path(r"detail/<tvshow>/", DetailView.as_view(), name="detail"),
    path(r"add/", AddView.as_view(), name="add"),
    path(r"", IndexView.as_view(), name="index"),
]
