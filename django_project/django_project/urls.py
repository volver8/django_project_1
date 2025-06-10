import os

from django.contrib import admin
from django.urls import include, path
from dotenv import load_dotenv


load_dotenv()


DEBUG = bool(os.getenv("DEBUG"))


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]

if DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
