from django.db import models
from blog.models import Post
from example.models import User


class Report(models.Model):
    reporter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity_type = models.IntegerField()
    entity_id = models.IntegerField()
    reason_type = models.IntegerField()



