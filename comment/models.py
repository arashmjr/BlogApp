from django.db import models
from blog.models import Post
from example.models import User


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    is_verified = models.BooleanField(default=False)
    has_replied = models.BooleanField(default=False)
    replied_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_ban = models.BooleanField(default=False)


