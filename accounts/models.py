from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, null=True)
    _class = models.PositiveIntegerField(null=True)
