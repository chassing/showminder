from django.conf.urls import url

from .views import DeleteNotificationView
from .views import UpdateView


urlpatterns = [
    url(r"^update/$", UpdateView.as_view(), name="update"),
    url(r"^deletenotification/(?P<pk>[0-9]+)/$", DeleteNotificationView.as_view(), name="delete-notification"),
]
