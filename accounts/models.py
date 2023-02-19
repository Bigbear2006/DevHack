from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, null=True)
    clas_s = models.PositiveIntegerField(null=True)

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])
