from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', verbose_name='Аватар', blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
