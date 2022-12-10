from rest_framework import serializers


class UserRegistrationPayloadSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    password_repeat = serializers.CharField()
    are_service_terms_approved = serializers.BooleanField(default=False)
