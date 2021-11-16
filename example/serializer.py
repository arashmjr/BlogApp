from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = ['id', 'username', 'email', 'password', 'date_joined']
        # exclude = ('password',)
        fields = "__all__"
