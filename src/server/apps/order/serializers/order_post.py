from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


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
    additional_info = serializers.CharField(required=False)
    products = serializers.ListField()
    sum = serializers.CharField()

    def validate_first_name(self, value):
        if value is None or value == '':
            raise serializers.ValidationError(
                _('First name cannot be empty!'),
                code='order__first_name_cannot_be_empty',
            )
        return value

    def validate_additional_info(self, value):
        if value is None:
            pass

    def validate_products(self, value):
        for product in value:
            if not isinstance(product, dict):
                    raise serializers.ValidationError(
                        _('Elements of the list must be dicts!'),
                        code='products_with_quantity__elements_must_be_dicts',
                    )
            try:
                if not isinstance(product['id'], int):
                    raise serializers.ValidationError(
                        _('Product id must be an integer!'),
                        code='product_with_quantity__id_must_be_int',
                    )
            except KeyError:
                raise serializers.ValidationError(
                        _('Product must have an id field!'),
                        code='product_with_quantity__no_id_field',
                    )
            try:
                if not isinstance(product['quantity'], int):
                    raise serializers.ValidationError(
                        _('Product quantity must be an integer!'),
                        code='product_with_quantity__quantity_must_be_int',
                    )
            except KeyError:
                raise serializers.ValidationError(
                        _('Product must have a quantity field!'),
                        code='product_with_quantity__no_quantity_field',
                    )
            if len(product) > 2:
                raise serializers.ValidationError(
                    _('Product must have only 2 fields: id and quantity!'),
                    code='product_with_quantity__to_many_fields',
                )
        return value
    
    def validate_are_service_terms_accepted(self, value):
        if value != True:
            raise serializers.ValidationError(
                _('Service terms must be accepted'),
                code='order__service_terms_not_accepted',
            )
        return value

    def validate_phone(self, value):
        for digit in value:
            if not digit.isnumeric():
                raise serializers.ValidationError(
                    _('Number must contain digits only!'),
                    code='order__phone_must_contain_only_digits',
                )
        return value

    def validate_house_number(self, value):
        for char in value:
            if char.isspace():
                raise serializers.ValidationError(
                    _('House number cannot contain spaces!'),
                    code='order__house_number_cannot_contain_space',
                )
        return value

    def validate_post_code(self, value):
        if len(value) != 6 or value[2] != '-':
            raise serializers.ValidationError(
                _('Post code format is incorrect!'),
                code='order__post_code_format_incorrect',
            )
        i = 0
        for digit in value:
            if not digit.isnumeric():
                if i != 2:
                    raise serializers.ValidationError(
                        _('Post code must contain digits in correct places!'),
                        code='order__post_code_must_contain_numbers_in_correct_places',
                    )
            i += 1
        return value
