from django.contrib.auth import get_user_model
from django.db import models
from blog.models import Post
import datetime


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.datetime.now)
    is_deleted = models.BooleanField(default=False)
