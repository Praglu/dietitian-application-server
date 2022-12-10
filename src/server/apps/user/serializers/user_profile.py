from django.contrib.auth.models import User

from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
        read_only_fields = fields
