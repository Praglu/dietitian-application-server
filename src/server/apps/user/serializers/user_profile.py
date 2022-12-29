from django.contrib.auth.models import User

from rest_framework import serializers

from server.apps.user.models import BonusUser


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta(object):
        model = BonusUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone',
            'street',
            'house_number',
            'city',
            'post_code',
        ]
        read_only_fields = fields
