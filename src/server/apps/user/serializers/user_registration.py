from rest_framework import serializers


class UserRegistrationPayloadSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    password_repeat = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    street = serializers.CharField()
    house_number = serializers.CharField()
    city = serializers.CharField()
    post_code = serializers.CharField()
    are_service_terms_approved = serializers.BooleanField(default=False)
