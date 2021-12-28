from django.db import models
from post.models import Post
from example.models import User
import uuid


class Comment(models.Model):
    id = models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    is_verified = models.BooleanField(default=False)
    has_replied = models.BooleanField(default=False)
    replied_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_ban = models.BooleanField(default=False)


