from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from example.models import User


author_group, created = Group.objects.get_or_create(name='author')

ct = ContentType.objects.get_for_model(User)

author_group.permissions.set()
author_group.permissions.add()
author_group.permissions.remove()
author_group.permissions.clear()

# Assign a user to groups
# author_group.user_set.add(user)


def is_author(user):
    return user.groups.filter(name='author').exists()
