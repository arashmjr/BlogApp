from django.contrib import admin
from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'content',
                    'is_verified', 'has_replied', 'replied_id', 'created_at',)
