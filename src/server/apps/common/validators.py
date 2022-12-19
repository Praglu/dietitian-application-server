from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy


class AtLeastOneDigitOrSpecialValidator(object):
    def __init__(self, password):
        self.password = password

    def _validate(self):
        if not any(
            [
                letter.isdigit() for letter in self.password
            ]
        ) and not self._is_special_character(self.password):
            raise ValidationError(
                _('Your password must contain at least one digit.'),
                code='user__password_requires_digit_or_special_character',
            )

    def _is_special_character(self, password):
        if any(letter in ''.join('!@#$%^&*()-_=+[{]}"|,<.>/?;:') for letter in password):
            return True


class AtLeastOneLowerValidator(object):
    def __init__(self, password):
        self.password = password
        self._validate()

    def _validate(self):
        if not any([letter.islower() for letter in self.password]):
            raise ValidationError(
                _('Your password must contain at least one lower letter.'),
                code='user__password_requires_lowercase_letter',
            )


class AtLeastOneUpperValidator(object):
    def __init__(self, password):
        self.password = password

    def validate(self):
        if not any([letter.isupper() for letter in self.password]):
            raise ValidationError(
                _('Your password must contain at least one upper letter.'),
                code='user__password_requires_uppercase_letter',
            )


class MinimumLengthValidator(object):
    def __init__(self, password, min_length=8):
        self.password = password
        self.min_length = min_length
        self._validate()

    def _validate(self):
        if len(self.password) < self.min_length:
            raise ValidationError(
                _('This password must contain at least %(min_length)d characters.'),  # noqa: WPS323
                code='user__password_too_short',
                params={'min_length': self.min_length},
            )


@deconstructible
class OnlyDigitsValidator(object):
    message = gettext_lazy('only_digits_validation_error')
    code = 'only_digits_validation_error'

    def __call__(self, value):
        try:
            int(value)
        except ValueError:
            raise ValidationError(self.message, code=self.code, params={})
