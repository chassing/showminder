from django.conf.urls import url

from .views import *  # noqa


urlpatterns = [
    url(r'^inc-season/(?P<tvshow>[0-9]+)/$', IncSeasonView.as_view(), name="inc-season"),
    url(r'^inc-episode/(?P<tvshow>[0-9]+)/$', IncEpisodeView.as_view(), name="inc-episode"),
    url(r'^detail/(?P<tvshow>[0-9]+)/$', DetailView.as_view(), name="detail"),
    url(r'^add/$', AddView.as_view(), name="add"),
    url(r'^$', IndexView.as_view(), name="index"),
]
