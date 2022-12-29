from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class WrongPasswordRepeatError(ValidationError):
    default_detail = 'user__wrong_password_repeat'
    _text = _('user__wrong_password_repeat')
    _title = _('user__wrong_password_repeat_title')
    default_code = default_detail


class PasswordTooShortError(ValidationError):
    default_detail = 'user__password_too_short'
    _text = _('user__password_too_short')
    _title = _('user__password_too_short_title')
    default_code = default_detail


class PasswordRequiresUpperCaseLetterError(ValidationError):
    default_detail = 'user__password_requires_uppercase_letter'
    _text = _('user__password_requires_uppercase_letter')
    _title = _('user__password_requires_uppercase_letter_title')
    default_code = default_detail


class PasswordRequiresLowerCaseLetterError(ValidationError):
    default_detail = 'user__password_requires_lowercase_letter'
    _text = _('user__password_requires_lowercase_letter')
    _title = _('user__password_requires_lowercase_letter_title')
    default_code = default_detail


class PasswordRequiresDigitOrSpecialCharacterError(ValidationError):
    default_detail = 'user__password_requires_digit_or_special_character'
    _text = _('user__password_requires_digit_or_special_character')
    _title = _('user__password_requires_digit_or_special_character_title')
    default_code = default_detail


class ServiceTermsNotApprovedError(ValidationError):
    default_detail = 'user__service_terms_are_not_approved'
    _text = _('user__service_terms_are_not_approved')
    _title = _('user__service_terms_are_not_approved_title')
    default_code = default_detail


class EmailFieldEmptyError(ValidationError):
    default_detail = 'user__email_field_cannot_be_empty'
    _text = _('user__email_field_cannot_be_empty')
    _title = _('user__email_field_cannot_be_empty_title')
    default_code = default_detail


class FirstNameFieldEmptyError(ValidationError):
    default_detail = 'user__first_name_field_cannot_be_empty'
    _text = _('user__first_name_field_cannot_be_empty')
    _title = _('user__first_name_field_cannot_be_empty_title')
    default_code = default_detail


class LastNameFieldEmptyError(ValidationError):
    default_detail = 'user__last_name_field_cannot_be_empty'
    _text = _('user__last_name_field_cannot_be_empty')
    _title = _('user__last_name_field_cannot_be_empty_title')
    default_code = default_detail
