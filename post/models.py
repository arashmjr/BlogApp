from django.db import models
from example.models import User
import uuid


class Post(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    post_title = models.CharField(max_length=40)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_ban = models.BooleanField(default=False)
