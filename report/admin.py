from django.contrib import admin
from report.models import ReportPost, ReportComment


@admin.register(ReportPost)
class ReportPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporter_user', 'post', 'reason_type')


@admin.register(ReportComment)
class ReportCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporter_user', 'comment', 'reason_type')

