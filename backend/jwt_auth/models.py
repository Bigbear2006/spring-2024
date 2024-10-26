from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='users', null=True, default='users/default.png')
    patronymic = models.CharField(max_length=150, blank=True)
    objects: models.Manager
