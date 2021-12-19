from django.db import models
from example.models import User
import uuid


class Report(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reporter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity_id = models.UUIDField()
    reason_type = models.IntegerField()






