from django.contrib import admin

from .models import ApiNotification


@admin.register(ApiNotification)
class ApiNotificationAdmin(admin.ModelAdmin):
    pass
