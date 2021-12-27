from django.urls import path

from .views import DeleteNotificationView, UpdateView

app_name = "api"

urlpatterns = [
    path(r"update/", UpdateView.as_view(), name="update"),
    path(r"deletenotification/<pk>/", DeleteNotificationView.as_view(), name="delete-notification"),
]
