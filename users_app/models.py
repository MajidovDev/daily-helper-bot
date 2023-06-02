from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    telegram_id = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return f"{self.username}"


