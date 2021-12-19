from django.contrib import admin
from report.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporter_user', 'entity_id', 'reason_type')


# @admin.register(ReportComment)
# class ReportCommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'reporter_user', 'comment', 'reason_type')

