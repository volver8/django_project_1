from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    login = models.SlugField("Номер телефона", unique=True, blank=False)
