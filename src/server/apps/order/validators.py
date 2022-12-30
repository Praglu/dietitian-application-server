from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


class ProductsJsonValidator(object):
    def __init__(self, value):
        self.value = value
        self._validate()

    def _validate(self):
        for product in self.value:
            if not isinstance(product, dict):
                raise ValidationError(
                    _('Elements of the list must be dicts!'),
                    code='products_with_quantity__elements_must_be_dicts',
                )
            try:
                if not isinstance(product['id'], int):
                    raise ValidationError(
                        _('Product id must be an integer!'),
                        code='product_with_quantity__id_must_be_int',
                    )
            except KeyError:
                raise ValidationError(
                        _('Product must have an id field!'),
                        code='product_with_quantity__no_id_field',
                    )
            try:
                if not isinstance(product['quantity'], int):
                    raise ValidationError(
                        _('Product quantity must be an integer!'),
                        code='product_with_quantity__quantity_must_be_int',
                    )
            except KeyError:
                raise ValidationError(
                        _('Product must have a quantity field!'),
                        code='product_with_quantity__no_quantity_field',
                    )
            if len(product) > 2:
                raise ValidationError(
                    _('Product must have only 2 fields: id and quantity!'),
                    code='product_with_quantity__to_many_fields',
                )
