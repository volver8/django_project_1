import os

from django.core.asgi import get_asgi_application

from .base import DEBUG


if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.staging")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.production")

application = get_asgi_application()
