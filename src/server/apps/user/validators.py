from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class AtLeastOneDigitOrSpecialValidator(object):
    def validate(self, password, user=None):
        if not any([letter.isdigit() for letter in password]) and not self._is_special_character(password):
            raise ValidationError(
                _('Your password must contain at least one digit.'),
                code='user__password_requires_digit_or_special_character',
            )

    def get_help_text(self):
        return _('Your password must contain at least one digit.')

    def _is_special_character(self, password):
        if any(letter in ''.join('!@#$%^&*()-_=+[{]}"|,<.>/?;:') for letter in password):
            return True


class AtLeastOneLowerValidator(object):
    def validate(self, password, user=None):
        if not any([letter.islower() for letter in password]):
            raise ValidationError(
                _('Your password must contain at least one lower letter.'),
                code='user__password_requires_lowercase_letter',
            )

    def get_help_text(self):
        return _('Your password must contain at least one lower letter.')


class AtLeastOneUpperValidator(object):
    def validate(self, password, user=None):
        if not any([letter.isupper() for letter in password]):
            raise ValidationError(
                _('Your password must contain at least one upper letter.'),
                code='user__password_requires_uppercase_letter',
            )

    def get_help_text(self):
        return _('Your password must contain at least one upper letter.')


class MinimumLengthValidator(object):
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _('This password must contain at least %(min_length)d characters.'),  # noqa: WPS323
                code='user__password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _('Your password must contain at least {min_length} characters.').format(
            min_length=self.min_length,
        )
