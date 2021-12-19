from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth import get_user_model
import uuid


class CustomUserManager(UserManager):
    pass


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    blog_title = models.CharField(max_length=40, blank=False, default='unknown')
