from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=120, default='', unique=True)
    email = models.EmailField(max_length=264)
    password = models.CharField(max_length=264)

    def __str__(self):
        return self.username
