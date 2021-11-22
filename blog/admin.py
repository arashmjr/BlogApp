from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'author', 'body',
                    'created_at', 'updated_at', 'is_ban')


