from django.db import models
from blog.models import Post


class Comment(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    is_verified = models.BooleanField(default=False)
    has_replied = models.BooleanField(default=False)
    replied_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
