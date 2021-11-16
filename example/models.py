from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth import get_user_model


class CustomUserManager(UserManager):
    pass


class User(AbstractUser):
    blog_title = models.CharField\
        (max_length=40,
         blank=False,
         default='unknown')
