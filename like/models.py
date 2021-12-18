from django.db import models
from post.models import Post
from example.models import User
import datetime


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    is_deleted = models.BooleanField(default=False)
