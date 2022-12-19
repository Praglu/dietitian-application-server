from rest_framework import serializers


class ContactFormPayloadSerializer(serializers.Serializer):
    first_and_last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    message = serializers.CharField()
