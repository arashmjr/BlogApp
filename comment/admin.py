from django.contrib import admin
from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'post', 'content',
                    'is_verified', 'has_replied', 'replied_id', 'created_at',)
