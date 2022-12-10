from drf_spectacular.utils import inline_serializer
from rest_framework import serializers


def exception_schema_dict(exceptions):
    return inline_serializer(
        str([exc.default_code for exc in exceptions]),
        fields={
            'error_code': serializers.CharField(),
            'error_title': serializers.CharField(),
            'error_message': serializers.CharField(),
            'invalid_fields': serializers.DictField(),
        },
    )
