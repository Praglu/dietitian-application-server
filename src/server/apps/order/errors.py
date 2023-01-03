from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class FirstNameContainsDigitsError(ValidationError):
    default_detail = 'Imię nie może zawierać cyfr'
    _text = _('Imię nie może zawierać cyfr')
    _title = _('Imię nie może zawierać cyfr')
    default_code = default_detail


class LastNameContainsDigitsError(ValidationError):
    default_detail = 'Nazwisko nie może zawierać cyfr'
    _text = _('Nazwisko nie może zawierać cyfr')
    _title = _('Nazwisko nie może zawierać cyfr')
    default_code = default_detail


class ProductsWithQuantityIsNotListError(ValidationError):
    default_detail = 'Elementy tablicy muszą być obiektami'
    _text = _('Elementy tablicy muszą być obiektami')
    _title = _('Elementy tablicy muszą być obiektami')
    default_code = default_detail


class ProductIdIsNotIntegerError(ValidationError):
    default_detail = 'Id produktu musi być liczbą naturalną'
    _text = _('Id produktu musi być liczbą naturalną')
    _title = _('Id produktu musi być liczbą naturalną')
    default_code = default_detail


class ProductQuantityIsNotIntegerError(ValidationError):
    default_detail = 'Ilość produktu musi być liczbą naturalną'
    _text = _('Ilość produktu musi być liczbą naturalną')
    _title = _('Ilość produktu musi być liczbą naturalną')
    default_code = default_detail


class ProductHasNoIdFieldError(ValidationError):
    default_detail = 'Obiekt produktów musi zawierać pole id'
    _text = _('Obiekt produktów musi zawierać pole id')
    _title = _('Obiekt produktów musi zawierać pole id')
    default_code = default_detail


class ProductHasNoQuantityFieldError(ValidationError):
    default_detail = 'Obiekt produktów musi zawierać pole quantity'
    _text = _('Obiekt produktów musi zawierać pole quantity')
    _title = _('Obiekt produktów musi zawierać pole quantity')
    default_code = default_detail


class ProductHasInvalidFieldsError(ValidationError):
    default_detail = 'Obiekt produktów może zawierać tylko pole id oraz quantity'
    _text = _('Obiekt produktów może zawierać tylko pole id oraz quantity')
    _title = _('Obiekt produktów może zawierać tylko pole id oraz quantity')
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


class SumIsNotNumberError(ValidationError):
    default_detail = 'Suma może zawierać tylko cyfry'
    _text = _('Suma może zawierać tylko cyfry')
    _title = _('Suma może zawierać tylko cyfry')
    default_code = default_detail


class IncorrectPaymentMethodError(ValidationError):
    default_detail = 'Wybraną metodą płatności musi być przelew tradycyjny'
    _text = _('Wybraną metodą płatności musi być przelew tradycyjny')
    _title = _('Wybraną metodą płatności musi być przelew tradycyjny')
    default_code = default_detail
