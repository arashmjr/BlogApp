from rest_framework import serializers
from report.models import Report
from rest_framework.serializers import ValidationError


class ReportSerializer(serializers.ModelSerializer):

    def validate_reason_type(self, reason_type):
        if reason_type >= 5:
            raise ValidationError("reason_type out of range")
        return reason_type

    class Meta:
        model = Report
        fields = "__all__"

























