from django.contrib import admin

from .models import *  # noqa


@admin.register(TvShow)
class TvShowAdmin(admin.ModelAdmin):  # noqa
    pass
