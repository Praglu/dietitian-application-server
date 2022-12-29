from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.response import Response

from server.apps.common.helpers_exception import exception_schema_dict
from server.apps.contactform.errors import (
    FirstAndLastNameFieldEmptyError,
    EmailFieldEmptyError,
    PhoneFieldEmptyError,
    MessageFieldEmptyError,
)
from server.apps.contactform.serializers import ContactFormPayloadSerializer
from server.datastore.commands.contact_form import ContactFormCommand


class ContactFormView(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    @extend_schema(
        request=ContactFormPayloadSerializer,
        responses={
            201: status.HTTP_201_CREATED,
            400: exception_schema_dict(
                (
                    FirstAndLastNameFieldEmptyError,
                    EmailFieldEmptyError,
                    PhoneFieldEmptyError,
                    MessageFieldEmptyError,
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
    def send_contact_form(self, request, **kwargs):
        payload_serializer = ContactFormPayloadSerializer(data=request.data)
        payload_serializer.is_valid(raise_exception=False)
        command = ContactFormCommand(
            first_and_last_name=payload_serializer.data['first_and_last_name'],
            email=payload_serializer.data['email'],
            phone=payload_serializer.data['phone'],
            message=payload_serializer.data['message']
        )
        command.send_contact_form()

        return Response(status=status.HTTP_201_CREATED)
