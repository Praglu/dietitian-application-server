from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class AtLeastOneUpperValidator(object):
    def validate(self, password, user=None):
        if not any([letter.isupper() for letter in password]):
            raise ValidationError(
                _('Your password must contain at least one upper letter.'),
                code='account__password_requires_uppercase_letter',
            )

    def get_help_text(self):
        return _('Your password must contain at least one upper letter.')
