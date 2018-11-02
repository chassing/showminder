from django.conf.urls import url

from .views import UpdateView


urlpatterns = [url(r"^update/$", UpdateView.as_view(), name="update")]
