from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.views import defaults as default_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # project urls
    path("api/", include("api.urls")),
    path("", include("frontend.urls")),
]
