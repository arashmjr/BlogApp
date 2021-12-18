from django.db import models
from post.models import Post
from example.models import User
from comment.models import Comment


class ReportPost(models.Model):
    reporter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason_type = models.IntegerField()


class ReportComment(models.Model):
    reporter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason_type = models.IntegerField()




