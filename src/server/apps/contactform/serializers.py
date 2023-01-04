from rest_framework import serializers

from server.apps.contactform.errors import (
    FirstAndLastNameContainsDigitsError,
    PhoneContainsNotDigitError,
)


class ContactFormPayloadSerializer(serializers.Serializer):
    first_and_last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    message = serializers.CharField()

    def validate_first_and_last_name(self, value):
        for char in value:
            if not char.isalpha():
                raise FirstAndLastNameContainsDigitsError
        return value

    def validate_phone(self, value):
        for digit in value:
            if not digit.isdigit():
                raise PhoneContainsNotDigitError
        return value
