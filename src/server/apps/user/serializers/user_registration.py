from django.contrib.auth.models import User
from rest_framework import serializers

from server.apps.user.errors import (
    EmailAlreadyExistsError,
    FirstNameContainsDigitsError,
    HouseNumberContainsSpacesError,
    LastNameContainsDigitsError,
    PostCodeDigitsInIncorrectPlacesError,
    PostCodeIncorrectFormatError,
    ServiceTermsNotAcceptedError,
    PasswordTooShortError,
    PasswordRequiresUpperCaseLetterError,
    PasswordRequiresDigitOrSpecialCharacterError,
    PasswordRequiresLowerCaseLetterError,
    PhoneContainsNotDigitsError,
    WrongPasswordRepeatError,
)


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

    def validate(self, data):
        if data['password'] == data['password_repeat']:
            return data
        raise WrongPasswordRepeatError

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            if user:
                raise EmailAlreadyExistsError
        except:
            return value

    def validate_password(self, value):
        if len(value) < 8:
            raise PasswordTooShortError
        if not any([letter.isupper() for letter in value]):
            raise PasswordRequiresUpperCaseLetterError
        if not any([letter.islower() for letter in value]):
            raise PasswordRequiresLowerCaseLetterError
        if not any([letter.isdigit() for letter in value]) and not self._is_special_character(value):
            raise PasswordRequiresDigitOrSpecialCharacterError
        return value
    
    def validate_first_name(self, value):
        for letter in value:
            if not letter.isalpha() and not letter.isspace():
                raise FirstNameContainsDigitsError
        return value

    def validate_last_name(self, value):
        for letter in value:
            if not letter.isalpha() and not letter.isspace():
                raise LastNameContainsDigitsError
        return value
    
    def validate_are_service_terms_approved(self, value):
        if value != True:
            raise ServiceTermsNotAcceptedError
        return value

    def validate_house_number(self, value):
        for char in value:
            if char.isspace():
                raise HouseNumberContainsSpacesError
        return value

    def validate_post_code(self, value):
        if len(value) != 6 or value[2] != '-':
            raise PostCodeIncorrectFormatError
        i = 0
        for digit in value:
            if not digit.isnumeric():
                if i != 2:
                    raise PostCodeDigitsInIncorrectPlacesError
            i += 1
        return value

    def _is_special_character(self, password):
        if any(letter in ''.join('!@#$%^&*()-_=+[{]}"|,<.>/?;:') for letter in password):
            return True

    def validate_phone(self, value):
        for digit in value:
            if not digit.isnumeric():
                raise PhoneContainsNotDigitsError
        return value

    def validate_city(self, value):
        for letter in value:
            if not letter.isalpha() and not letter.isspace():
                raise LastNameContainsDigitsError
        return value
