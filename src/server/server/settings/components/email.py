import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = os.getenv('EMAIL_PORT', '')
# only one can be set true
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', False)  # noqa: WPS425
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', False)  # noqa: WPS425

LOGGING_EMAIL_HOST = os.getenv('LOGGING_EMAIL_HOST', '')
LOGGING_EMAIL_HOST_USER = os.getenv('LOGGING_EMAIL_HOST_USER', '')
LOGGING_EMAIL_HOST_PASSWORD = os.getenv('LOGGING_EMAIL_HOST_PASSWORD', '')
LOGGING_EMAIL_PORT = os.getenv('LOGGING_EMAIL_PORT', '')
LOGGING_EMAIL_RECEIVERS_LIST = os.getenv('LOGGING_EMAIL_RECEIVERS_LIST', LOGGING_EMAIL_HOST_USER)
# only one can be set true
LOGGING_EMAIL_USE_SSL = os.getenv('LOGGING_EMAIL_USE_SSL', False)  # noqa: WPS425
LOGGING_EMAIL_USE_TLS = os.getenv('LOGGING_EMAIL_USE_TLS', False)  # noqa: WPS425


ADMIN_EMAIL = EMAIL_HOST_USER
SUPPORT_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = ADMIN_EMAIL
SERVER_EMAIL = ADMIN_EMAIL
