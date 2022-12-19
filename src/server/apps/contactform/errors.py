from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class FirstAndLastNameFieldEmptyError(ValidationError):
    default_detail = 'contactform__first_and_last_name_field_cannot_be_empty'
    _text = _('contactform__first_and_last_name_field_cannot_be_empty')
    _title = _('contactform__first_and_last_name_field_cannot_be_empty_title')
    default_code = default_detail


class EmailFieldEmptyError(ValidationError):
    default_detail = 'contactform__email_field_cannot_be_empty'
    _text = _('contactform__email_field_cannot_be_empty')
    _title = _('contactform__email_field_cannot_be_empty_title')
    default_code = default_detail


class PhoneFieldEmptyError(ValidationError):
    default_detail = 'contactform__phone_field_cannot_be_empty'
    _text = _('contactform__phone_field_cannot_be_empty')
    _title = _('contactform__phone_field_cannot_be_empty_title')
    default_code = default_detail


class MessageFieldEmptyError(ValidationError):
    default_detail = 'contactform__message_field_cannot_be_empty'
    _text = _('contactform__message_field_cannot_be_empty')
    _title = _('contactform__message_field_cannot_be_empty_title')
    default_code = default_detail
