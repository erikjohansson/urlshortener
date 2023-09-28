from django.contrib import admin
from shortener.models import Shorturl


@admin.register(Shorturl)
class ShorturlAdmin(admin.ModelAdmin):
    list_display = ("identifier", "url", "user", "created")
    readonly_fields = ("identifier", "created")
