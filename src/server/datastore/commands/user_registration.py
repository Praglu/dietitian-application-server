from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import get_default_password_validators
from django.core.exceptions import ValidationError

from server.apps.user.enums import UserGroup
from server.apps.user.errors import (
    EmailFieldEmptyError,
    FirstNameFieldEmptyError,
    LastNameFieldEmptyError,
    PasswordRequiresDigitOrSpecialCharacterError,
    PasswordRequiresLowerCaseLetterError,
    PasswordRequiresUpperCaseLetterError,
    PasswordTooShortError,
    ServiceTermsNotApprovedError,
    WrongPasswordRepeatError,
)
from server.apps.user.models import BonusUser
from server.datastore.commands.abstract import AbstractCommand


class UserRegistrationCommand(AbstractCommand):
    rest_errors = {
        'user__password_too_short': PasswordTooShortError,
        'user__password_requires_uppercase_letter': PasswordRequiresUpperCaseLetterError,
        'user__password_requires_lowercase_letter': PasswordRequiresLowerCaseLetterError,
        'user__password_requires_digit_or_special_character': PasswordRequiresDigitOrSpecialCharacterError,
    }

    def __init__(
        self, 
        email,
        password,
        password_repeat,
        first_name,
        last_name,
        phone,
        street,
        house_number,
        city,
        post_code,
        are_service_terms_approved
    ):  # noqa: WPS211
        self.email = email
        self.password = password
        self.password_repeat = password_repeat
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.street = street
        self.house_number = house_number
        self.city = city
        self.post_code = post_code
        self.are_service_terms_approved = are_service_terms_approved

    def register_user(self):
        self._validate_passwords()
        self._validate_fields()
        self._check_service_terms()
        self._create_user()
        self._add_user_to_group()
        self.user.save()

    def _validate_passwords(self):
        if self.password != self.password_repeat:
            raise WrongPasswordRepeatError
        self._validate_password()

    def _validate_fields(self):
        if not self.email:
            raise EmailFieldEmptyError
        if not self.first_name:
            raise FirstNameFieldEmptyError
        if not self.last_name:
            raise LastNameFieldEmptyError

    def _check_service_terms(self):
        if not self.are_service_terms_approved:
            raise ServiceTermsNotApprovedError

    def _create_user(self):
        self.user = get_user_model().objects.create_user(
            username=self.email,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=True,
            is_staff=False,
        )
        self.user.set_password(self.password)
        self.user.save()

        self.bonus_user = BonusUser.objects.create(
            user=self.user,
            phone=self.phone,
            street=self.street,
            house_number=self.house_number,
            city=self.city,
            post_code=self.post_code,
        )
        self.bonus_user.save()

    def _add_user_to_group(self):
        try:
            self.customer_group = Group.objects.get(name=UserGroup.CUSTOMER.value)
            self.user.groups.add(self.customer_group)
            self.user.save()
        except:
            pass

    def _validate_password(self, user=None, password_validators=None):
        if password_validators is None:
            password_validators = get_default_password_validators()
        for validator in password_validators:
            try:
                validator.validate(self.password, user)
            except ValidationError as error:
                raise self.rest_errors.get(error.code)
