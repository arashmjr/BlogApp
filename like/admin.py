from django.contrib import admin
from like.models import Like


@admin.register(Like)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at', 'is_deleted')
