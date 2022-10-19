from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MinimumLengthValidator(object):
    def __init__(self, min_length=11):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _('This password must contain at least %(min_length)d characters.'),  # noqa: WPS323
                code='account__password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _('Your password must contain at least {min_length} characters.').format(
            min_length=self.min_length,
        )
