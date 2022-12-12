from django.contrib.auth.models import User

from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from server.apps.common.helpers_exception import exception_schema_dict
from server.apps.user.errors import (
    PasswordRequiresDigitOrSpecialCharacterError,
    PasswordRequiresLowerCaseLetterError,
    PasswordRequiresUpperCaseLetterError,
    PasswordTooShortError,
    ServiceTermsNotApprovedError,
    WrongPasswordRepeatError,
)
from server.apps.user.permissions import IsCustomerPermission
from server.apps.user.serializers.user_profile import UserProfileSerializer
from server.apps.user.serializers.user_registration import UserRegistrationPayloadSerializer
from server.datastore.commands.user_registration import UserRegistrationCommand


class ApiUserRegistrationView(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    @extend_schema(
        request=UserRegistrationPayloadSerializer,
        responses={
            204: None,
            400: exception_schema_dict(
                (
                    PasswordRequiresDigitOrSpecialCharacterError,
                    PasswordRequiresLowerCaseLetterError,
                    PasswordRequiresUpperCaseLetterError,
                    PasswordTooShortError,
                    ServiceTermsNotApprovedError,
                    WrongPasswordRepeatError,
                ),
            ),
            401: exception_schema_dict(
                (
                    NotAuthenticated,
                ),
            ),
            403: exception_schema_dict(
                (
                    PermissionDenied,
                ),
            ),
        },
    )
    @action(
        detail=True,
        methods=['post'],
    )
    def register_user(self, request, **kwargs):
        payload_serializer = UserRegistrationPayloadSerializer(data=request.data)
        payload_serializer.is_valid(raise_exception=True)
        command = UserRegistrationCommand(
            email=payload_serializer.data['email'],
            first_name=payload_serializer.data['first_name'],
            last_name=payload_serializer.data['last_name'],
            password=payload_serializer.data['password'],
            password_repeat=payload_serializer.data['password_repeat'],
            are_service_terms_approved=payload_serializer.data['are_service_terms_approved'],
        )
        command.register_user()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @extend_schema(
        responses={
            200: UserProfileSerializer,
            401: exception_schema_dict(
                (
                    NotAuthenticated,
                ),
            ),
            403: exception_schema_dict(
                (
                    PermissionDenied,
                ),
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)