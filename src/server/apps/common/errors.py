from enum import Enum

from rest_framework.exceptions import ValidationError


class CommonErrorsEnum(Enum):
    ERROR = 'error'
    MISSING = 'missing'
    ALREADY_EXISTS = 'already_exists'


class SerializerValidationError(ValidationError):
    default_code = 'validation_error'
