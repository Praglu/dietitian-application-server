import logging

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response

from server.apps.common.errors import SerializerValidationError

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    return get_server_error_response(exc)


def get_error_code_title(error_code):
    return '{error_code}_title'.format(error_code=error_code)


def get_server_error_response(exc):  # noqa: WPS210
    error_code = 'unknown_error'
    status_code = 500

    if isinstance(exc, APIException):
        error_code = exc.default_code
        status_code = exc.status_code

    logger.exception(exc)
    error_code_title_key = get_error_code_title(error_code)
    response_data = {
        'error_code': error_code,
        'error_title': exc._title if getattr(exc, '_title', None) else _(error_code_title_key),  # noqa: WPS437
        'error_message': exc._text if getattr(exc, '_text', None) else _(error_code),  # noqa: WPS437
    }
    if getattr(exc, 'params', None):
        response_data['error_message'] = response_data['error_message'].format(**exc.params)
    if type(exc) is ValidationError:  # noqa: WPS516
        invalid_fields = {}
        for key in exc.detail.keys():
            invalid_fields[key] = str(exc.detail[key][0])
        if invalid_fields:
            response_data['error_code'] = SerializerValidationError.default_code
            response_data['error_title'] = ''
            response_data['error_message'] = ''
            response_data['invalid_fields'] = invalid_fields
    return Response(data=response_data, status=status_code)
