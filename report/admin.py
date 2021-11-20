from django.contrib import admin
from report.models import Report


@admin.register()
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'reporter_user')


