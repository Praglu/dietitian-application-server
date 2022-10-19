from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class AtLeastOneDigitValidator(object):
    def validate(self, password, user=None):
        if not any([letter.isdigit() for letter in password]):
            raise ValidationError(
                _('Your password must contain at least one digit.'),
                code='account__password_requires_digit',
            )

    def get_help_text(self):
        return _('Your password must contain at least one digit.')
