"""
URL configuration for coreapp project.
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.static import serve

from shortener.views import home_view, shorturl_detail, shorturl_list, shorturl_delete


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", shorturl_list, name="shorturl_list"),
    path("delete/", shorturl_delete, name="shorturl_delete"),
    path(
        "favicon.ico",
        serve,
        {"path": "img/favicon.ico", "document_root": settings.STATIC_ROOT},
    ),
    path("<identifier>", shorturl_detail, name="shorturl_detail"),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
