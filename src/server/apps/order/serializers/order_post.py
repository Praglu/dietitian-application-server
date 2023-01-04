from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from server.apps.order.errors import (
    FirstNameContainsDigitsError,
    LastNameContainsDigitsError,
    HouseNumberContainsSpacesError,
    PostCodeDigitsInIncorrectPlacesError,
    PostCodeIncorrectFormatError,
    PhoneContainsNotDigitsError,
    ServiceTermsNotAcceptedError,
    ProductHasInvalidFieldsError,
    ProductHasNoIdFieldError,
    ProductHasNoQuantityFieldError,
    ProductIdIsNotIntegerError,
    ProductQuantityIsNotIntegerError,
    ProductsWithQuantityIsNotListError,
    IncorrectPaymentMethodError,
    SumIsNotNumberError,
)


class OrderPayloadSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    street = serializers.CharField()
    house_number = serializers.CharField()
    post_code = serializers.CharField()
    city = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    are_service_terms_accepted = serializers.BooleanField(default=False)
    additional_info = serializers.CharField()
    products = serializers.ListField()
    payment_method = serializers.CharField()
    sum = serializers.CharField()

    def validate_first_name(self, value):
        for letter in value:
            if letter.isalpha():
                raise FirstNameContainsDigitsError
        return value

    def validate_last_name(self, value):
        for letter in value:
            if not letter.isalpha():
                raise LastNameContainsDigitsError
        return value

    def validate_products(self, value):
        for product in value:
            if not isinstance(product, dict):
                    raise ProductsWithQuantityIsNotListError
            try:
                if not isinstance(product['id'], int):
                    raise ProductIdIsNotIntegerError
            except KeyError:
                raise ProductHasNoIdFieldError
            try:
                if not isinstance(product['quantity'], int):
                    raise ProductQuantityIsNotIntegerError
            except KeyError:
                raise ProductHasNoQuantityFieldError
            if len(product) > 2:
                raise ProductHasInvalidFieldsError
        return value
    
    def validate_are_service_terms_accepted(self, value):
        if value != True:
            raise ServiceTermsNotAcceptedError
        return value

    def validate_phone(self, value):
        for digit in value:
            if not digit.isnumeric():
                raise PhoneContainsNotDigitsError
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

    def validate_payment_method(self, value):
        if value != 'Przelew tradycyjny':
            raise IncorrectPaymentMethodError
        return value

    def validate_sum(self, value):
        for digit in value:
            if not digit.isdigit() and not digit == ',':
                raise SumIsNotNumberError
        return value
