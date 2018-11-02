from django.contrib import admin

from .models import TvShow


@admin.register(TvShow)
class TvShowAdmin(admin.ModelAdmin):
    readonly_fields = ("last_seen",)
