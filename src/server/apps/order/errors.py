from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class FirstNameContainsDigitsError(ValidationError):
    default_detail = 'order__first_name_cannot_contain_digits'
    _text = _('Imię nie może zawierać cyfr')
    _title = _('Imię nie może zawierać cyfr')
    default_code = default_detail


class LastNameContainsDigitsError(ValidationError):
    default_detail = 'order__last_name_cannot_contain_digits'
    _text = _('Nazwisko nie może zawierać cyfr')
    _title = _('Nazwisko nie może zawierać cyfr')
    default_code = default_detail


class ProductsWithQuantityIsNotListError(ValidationError):
    default_detail = 'order__elements_of_the_list_must_be_dicts'
    _text = _('Elementy tablicy muszą być obiektami')
    _title = _('Elementy tablicy muszą być obiektami')
    default_code = default_detail


class ProductIdIsNotIntegerError(ValidationError):
    default_detail = 'order__product_id_must_be_integer'
    _text = _('Id produktu musi być liczbą naturalną')
    _title = _('Id produktu musi być liczbą naturalną')
    default_code = default_detail


class ProductQuantityIsNotIntegerError(ValidationError):
    default_detail = 'order__product_quantity_must_be_integer'
    _text = _('Ilość produktu musi być liczbą naturalną')
    _title = _('Ilość produktu musi być liczbą naturalną')
    default_code = default_detail


class ProductHasNoIdFieldError(ValidationError):
    default_detail = 'order__product_must_contain_id_field'
    _text = _('Obiekt produktów musi zawierać pole id')
    _title = _('Obiekt produktów musi zawierać pole id')
    default_code = default_detail


class ProductHasNoQuantityFieldError(ValidationError):
    default_detail = 'order__product_must_contain_quantity_field'
    _text = _('Obiekt produktów musi zawierać pole quantity')
    _title = _('Obiekt produktów musi zawierać pole quantity')
    default_code = default_detail


class ProductHasInvalidFieldsError(ValidationError):
    default_detail = 'order__product_must_contain_only_id_and_quantity'
    _text = _('Obiekt produktów może zawierać tylko pole id oraz quantity')
    _title = _('Obiekt produktów może zawierać tylko pole id oraz quantity')
    default_code = default_detail


class ServiceTermsNotAcceptedError(ValidationError):
    default_detail = 'order__service_terms_are_not_accepted'
    _text = _('Regulamin musi zostać zaakceptowany')
    _title = _('Regulamin musi zostać zaakceptowany')
    default_code = default_detail


class PhoneContainsNotDigitsError(ValidationError):
    default_detail = 'order__phone_must_contain_digits_only'
    _text = _('Numer telefonu może zawierać tylko cyfry')
    _title = _('Numer telefonu może zawierać tylko cyfry')
    default_code = default_detail


class HouseNumberContainsSpaces(ValidationError):
    default_detail = 'order__house_number_contains_spaces'
    _text = _('Numer budynku nie może zawierać spacji')
    _title = _('Numer budynku nie może zawierać spacji')
    default_code = default_detail


class PostCodeIncorrectFormatError(ValidationError):
    default_detail = 'order__post_code_incorrect_format'
    _text = _('Format kodu pocztowego jest nieprawidłowy')
    _title = _('Format kodu pocztowego jest nieprawidłowy')
    default_code = default_detail


class PostCodeDigitsInIncorrectPlacesError(ValidationError):
    default_detail = 'order__post_code_must_contain_digits_in_correct_places'
    _text = _('Kod pocztowy musi zawierać cyfry w odpowiednich miejscach')
    _title = _('Kod pocztowy musi zawierać cyfry w odpowiednich miejscach')
    default_code = default_detail


class SumIsNotNumberError(ValidationError):
    default_detail = 'order__sum_must_contain_digits_only'
    _text = _('Suma może zawierać tylko cyfry')
    _title = _('Suma może zawierać tylko cyfry')
    default_code = default_detail


class IncorrectPaymentMethodError(ValidationError):
    default_detail = 'order__chosen_payment_method_is_incorrect'
    _text = _('Wybraną metodą płatności musi być przelew tradycyjny')
    _title = _('Wybraną metodą płatności musi być przelew tradycyjny')
    default_code = default_detail
