from django.db import models
import datetime
from example.models import User
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField(max_length=40)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
