from rest_framework import serializers
from report.models import Report
from rest_framework.serializers import ValidationError
from blog.models import Post
from comment.models import Comment


class ReportSerializer(serializers.ModelSerializer):

    # reporter_user = serializers.IntegerField()
    entity_type = serializers.IntegerField()
    entity_id = serializers.IntegerField()
    reason_type = serializers.IntegerField()


    def validate_entity_type(self, entity_type):
        if entity_type >= 2:
            raise ValidationError("entity type out of range")

        return entity_type


    def validate_reason_type(self, reason_type):
        if reason_type >= 5:
            raise ValidationError("reason_type out of range")

    def validate(self, data):

        entity = data['entity_id']
        entity_type = data['entity_type']
        if entity_type == 0:
            for item in Post.objects.all():
                if item.id == entity:
                    return data
            raise ValidationError("entity_id does not exist")

        if entity_type == 1:
            for item in Comment.objects.all():
                if item.id == entity:
                    return data
            raise ValidationError("entity_id does not exist")

    class Meta:
        model = Report
        fields = ('reporter_user', 'entity_id', 'entity_type', 'reason_type')


















