from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class WrongPasswordRepeatError(ValidationError):
    default_detail = 'user__wrong_password_repeat'
    _text = _('Powtórzone hasła się nie zgadzają')
    _title = _('Powtórzone hasła się nie zgadzają')
    default_code = default_detail


class PasswordTooShortError(ValidationError):
    default_detail = 'user__password_too_short'
    _text = _('Hasło jest za krótkie')
    _title = _('Hasło jest za krótkie')
    default_code = default_detail


class PasswordRequiresUpperCaseLetterError(ValidationError):
    default_detail = 'user__password_requires_uppercase_letter'
    _text = _('Hasło wymaga wielkich liter')
    _title = _('Hasło wymaga wielkich liter')
    default_code = default_detail


class PasswordRequiresLowerCaseLetterError(ValidationError):
    default_detail = 'user__password_requires_lowercase_letter'
    _text = _('Hasło wymaga małych liter')
    _title = _('Hasło wymaga małych liter')
    default_code = default_detail


class PasswordRequiresDigitOrSpecialCharacterError(ValidationError):
    default_detail = 'user__password_requires_digit_or_special_character'
    _text = _('Hasło wymaga cyfry lub znaku specjalnego')
    _title = _('Hasło wymaga cyfry lub znaku specjalnego')
    default_code = default_detail


class ServiceTermsNotApprovedError(ValidationError):
    default_detail = 'user__service_terms_are_not_approved'
    _text = _('Regulamin nie został zaakceptowany')
    _title = _('Regulamin nie został zaakceptowany')
    default_code = default_detail


class EmailFieldEmptyError(ValidationError):
    default_detail = 'user__email_field_cannot_be_empty'
    _text = _('Pole email nie może być puste')
    _title = _('Pole email nie może być puste')
    default_code = default_detail


class FirstNameFieldEmptyError(ValidationError):
    default_detail = 'user__first_name_field_cannot_be_empty'
    _text = _('Pole imię nie może być puste')
    _title = _('Pole imię nie może być puste')
    default_code = default_detail


class LastNameFieldEmptyError(ValidationError):
    default_detail = 'user__last_name_field_cannot_be_empty'
    _text = _('Pole nazwisko nie może być puste')
    _title = _('Pole nazwisko nie może być puste')
    default_code = default_detail
