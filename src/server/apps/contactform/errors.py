from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class FirstAndLastNameContainsDigitsError(ValidationError):
    default_detail = 'Imię i nazwisko nie mogą zawierać cyfr ani znaków specjalnych'
    _text = _('Imię i nazwisko nie mogą zawierać cyfr ani znaków specjalnych')
    _title = _('Imię i nazwisko nie mogą zawierać cyfr ani znaków specjalnych')
    default_code = default_detail


class PhoneContainsNotDigitError(ValidationError):
    default_detail = 'Numer telefonu może zawierać tylko cyfry'
    _text = _('Numer telefonu może zawierać tylko cyfry')
    _title = _('Numer telefonu może zawierać tylko cyfry')
    default_code = default_detail
