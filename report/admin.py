from django.contrib import admin
from report.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporter_user', 'entity_id', 'entity_type', 'reason_type')


