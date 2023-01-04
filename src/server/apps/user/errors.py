from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class WrongPasswordRepeatError(ValidationError):
    default_detail = 'Powtórzone hasła się nie zgadzają'
    _text = _('Powtórzone hasła się nie zgadzają')
    _title = _('Powtórzone hasła się nie zgadzają')
    default_code = default_detail


class PasswordTooShortError(ValidationError):
    default_detail = 'Hasło jest za krótkie'
    _text = _('Hasło jest za krótkie')
    _title = _('Hasło jest za krótkie')
    default_code = default_detail


class PasswordRequiresUpperCaseLetterError(ValidationError):
    default_detail = 'Hasło wymaga wielkich liter'
    _text = _('Hasło wymaga wielkich liter')
    _title = _('Hasło wymaga wielkich liter')
    default_code = default_detail


class PasswordRequiresLowerCaseLetterError(ValidationError):
    default_detail = 'Hasło wymaga małych liter'
    _text = _('Hasło wymaga małych liter')
    _title = _('Hasło wymaga małych liter')
    default_code = default_detail


class PasswordRequiresDigitOrSpecialCharacterError(ValidationError):
    default_detail = 'Hasło wymaga cyfry lub znaku specjalnego'
    _text = _('Hasło wymaga cyfry lub znaku specjalnego')
    _title = _('Hasło wymaga cyfry lub znaku specjalnego')
    default_code = default_detail


class ServiceTermsNotApprovedError(ValidationError):
    default_detail = 'Regulamin nie został zaakceptowany'
    _text = _('Regulamin nie został zaakceptowany')
    _title = _('Regulamin nie został zaakceptowany')
    default_code = default_detail


class EmailFieldEmptyError(ValidationError):
    default_detail = 'Pole email nie może być puste'
    _text = _('Pole email nie może być puste')
    _title = _('Pole email nie może być puste')
    default_code = default_detail


class FirstNameFieldEmptyError(ValidationError):
    default_detail = 'Pole imię nie może być puste'
    _text = _('Pole imię nie może być puste')
    _title = _('Pole imię nie może być puste')
    default_code = default_detail


class LastNameFieldEmptyError(ValidationError):
    default_detail = 'Pole nazwisko nie może być puste'
    _text = _('Pole nazwisko nie może być puste')
    _title = _('Pole nazwisko nie może być puste')
    default_code = default_detail


class FirstNameContainsDigitsError(ValidationError):
    default_detail = 'Imię nie może zawierać cyfr lub znaków specjalnych'
    _text = _('Imię nie może zawierać cyfr lub znaków specjalnych')
    _title = _('Imię nie może zawierać cyfr lub znaków specjalnych')
    default_code = default_detail


class LastNameContainsDigitsError(ValidationError):
    default_detail = 'Nazwisko nie może zawierać cyfr lub znaków specjalnych'
    _text = _('Nazwisko nie może zawierać cyfr lub znaków specjalnych')
    _title = _('Nazwisko nie może zawierać cyfr lub znaków specjalnych')
    default_code = default_detail


class ServiceTermsNotAcceptedError(ValidationError):
    default_detail = 'Regulamin musi zostać zaakceptowany'
    _text = _('Regulamin musi zostać zaakceptowany')
    _title = _('Regulamin musi zostać zaakceptowany')
    default_code = default_detail


class PhoneContainsNotDigitsError(ValidationError):
    default_detail = 'Numer telefonu może zawierać tylko cyfry'
    _text = _('Numer telefonu może zawierać tylko cyfry')
    _title = _('Numer telefonu może zawierać tylko cyfry')
    default_code = default_detail


class HouseNumberContainsSpacesError(ValidationError):
    default_detail = 'Numer budynku nie może zawierać spacji'
    _text = _('Numer budynku nie może zawierać spacji')
    _title = _('Numer budynku nie może zawierać spacji')
    default_code = default_detail


class PostCodeIncorrectFormatError(ValidationError):
    default_detail = 'Format kodu pocztowego jest nieprawidłowy'
    _text = _('Format kodu pocztowego jest nieprawidłowy')
    _title = _('Format kodu pocztowego jest nieprawidłowy')
    default_code = default_detail


class PostCodeDigitsInIncorrectPlacesError(ValidationError):
    default_detail = 'Kod pocztowy musi zawierać cyfry w odpowiednich miejscach'
    _text = _('Kod pocztowy musi zawierać cyfry w odpowiednich miejscach')
    _title = _('Kod pocztowy musi zawierać cyfry w odpowiednich miejscach')
    default_code = default_detail


class PhoneContainsNotDigitsError(ValidationError):
    default_detail = 'Numer telefonu może zawierać tylko cyfry'
    _text = _('Numer telefonu może zawierać tylko cyfry')
    _title = _('Numer telefonu może zawierać tylko cyfry')
    default_code = default_detail


class CityContainsDigitsError(ValidationError):
    default_detail = 'Miasto nie może zawierać cyfr lub znaków specjalnych'
    _text = _('Miasto nie może zawierać cyfr lub znaków specjalnych')
    _title = _('Miasto nie może zawierać cyfr lub znaków specjalnych')
    default_code = default_detail