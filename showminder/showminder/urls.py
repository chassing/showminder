from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # project urls
    path("api/", include("api.urls")),
    path("", include("frontend.urls")),
]
