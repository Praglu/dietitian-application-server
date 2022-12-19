from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy


@deconstructible
class OnlyDigitsValidator(object):
    message = gettext_lazy('only_digits_validation_error')
    code = 'only_digits_validation_error'

    def __call__(self, value):
        try:
            int(value)
        except ValueError:
            raise ValidationError(self.message, code=self.code, params={})
