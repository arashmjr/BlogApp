from django.db import models
from blog.models import Post
from example.models import User
import datetime


class Report(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    entity_id = models.IntegerField()
    entity_type = models.IntegerField()
    reason_type = models.IntegerField()
    reporter_user = models.ForeignKey(User, on_delete=models.CASCADE)


