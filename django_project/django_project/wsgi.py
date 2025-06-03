import os

from django.conf.global_settings import DEBUG
from django.core.wsgi import get_wsgi_application


if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.staging")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.production")


application = get_wsgi_application()
