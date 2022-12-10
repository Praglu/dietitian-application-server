from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.viewsets import ViewSetMixin, reverse

from server.apps.user.enums import UserGroup
from server.apps.user.errors import (
    PasswordRequiresDigitOrSpecialCharacterError,
    PasswordRequiresLowerCaseLetterError,
    PasswordRequiresUpperCaseLetterError,
    PasswordTooShortError,
    ServiceTermsNotApprovedError,
    WrongPasswordRepeatError,
)


class TestCustomerRegistration(APITestCase, ViewSetMixin):  # noqa: WPS230
    def setUp(self):
        self.password = 'pass1234!'
        self.first_name = 'John'
        self.last_name = 'Wick'
        self.email = 'johnwick@sirocco.com'

        self.group_customer = Group.objects.get_or_create(name=UserGroup.CUSTOMER.value)[0]

        self.user_registration_url = reverse(
            'user_registration',
        )

    def test_user_registration_passwords_not_equal_fail(self):

        payload = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'tesT1234',
            'password_repeat': '1235test',
            'are_service_terms_approved': True,
        }

        response = self.client.post(self.user_registration_url, data=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['error_code'] == WrongPasswordRepeatError.default_code

    def test_user_registration_password_too_short_fail(self):

        payload = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'tesT12',
            'password_repeat': 'tesT12',
            'are_service_terms_approved': True,
        }

        response = self.client.post(self.user_registration_url, data=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['error_code'] == PasswordTooShortError.default_code

    def test_user_registration_password_no_uppercase_letter_fail(self):

        payload = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'test1234',
            'password_repeat': 'test1234',
            'are_service_terms_approved': True,
        }

        response = self.client.post(self.user_registration_url, data=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['error_code'] == PasswordRequiresUpperCaseLetterError.default_code

    def test_user_registration_password_no_lowercase_letter_fail(self):

        payload = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'TEST1234',
            'password_repeat': 'TEST1234',
            'are_service_terms_approved': True,
        }

        response = self.client.post(self.user_registration_url, data=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['error_code'] == PasswordRequiresLowerCaseLetterError.default_code

    def test_user_registration_password_no_digit_no_special_character_fail(self):

        payload = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'TestTestTest',
            'password_repeat': 'TestTestTest',
            'are_service_terms_approved': True,
        }

        response = self.client.post(self.user_registration_url, data=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['error_code'] == PasswordRequiresDigitOrSpecialCharacterError.default_code

    def test_user_registration_password_no_special_character_with_digit_success(self):

        payload = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'tesT1234',
            'password_repeat': 'tesT1234',
            'are_service_terms_approved': True,
        }

        response = self.client.post(self.user_registration_url, data=payload)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        current_user = User.objects.filter(username=payload['email']).first()
        assert check_password(password=payload['password'], encoded=current_user.password)
        assert current_user.groups.filter(name=UserGroup.CUSTOMER.value).exists()

    def test_user_registration_password_no_digit_with_special_character_success(self):

        payload = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'tesT@#$%',
            'password_repeat': 'tesT@#$%',
            'are_service_terms_approved': True,
        }

        response = self.client.post(self.user_registration_url, data=payload)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        current_user = User.objects.filter(username=payload['email']).first()
        assert check_password(password=payload['password'], encoded=current_user.password)
        assert current_user.groups.filter(name=UserGroup.CUSTOMER.value).exists()

    def test_user_registration_service_terms_not_approved_fail(self):

        payload = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'tesT1234',
            'password_repeat': 'tesT1234',
            'are_service_terms_approved': False,
        }

        response = self.client.post(self.user_registration_url, data=payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['error_code'] == ServiceTermsNotApprovedError.default_code
