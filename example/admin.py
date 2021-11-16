from django.contrib import admin
from example.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class SaveUser(UserAdmin):
    list_display = ('id', 'username', 'email', 'blog_title',)

