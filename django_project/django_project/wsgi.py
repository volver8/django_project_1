import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv


load_dotenv()

DEBUG = bool(os.getenv("DEBUG"))


if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.staging")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.production")

application = get_wsgi_application()
