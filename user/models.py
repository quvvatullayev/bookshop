from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class AuthUser(AbstractBaseUser):
    name = models.CharField(max_length=30)
    tg_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name