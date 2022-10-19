import os
from datetime import timedelta

JWT_SIGNING_KEY = os.getenv('JWT_SIGNING_KEY')

JWT_TOKEN_TYPE = os.getenv('JWT_TOKEN_TYPE', 'Bearer')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS512')

ACCESS_TOKEN_EXPIRE_SECONDS = int(os.getenv('ACCESS_TOKEN_EXPIRE_SECONDS', 60 * 5))
REFRESH_TOKEN_EXPIRE_SECONDS = int(os.getenv('REFRESH_TOKEN_EXPIRE_SECONDS', 60 * 60))

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': os.getenv('API_ANON_RATE_LIMITER'),
        'user': os.getenv('API_USER_RATE_LIMITER'),
    },
    'EXCEPTION_HANDLER': 'server.apps.common.exceptions.custom_exception_handler',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS),
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=REFRESH_TOKEN_EXPIRE_SECONDS),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS512',
    'SIGNING_KEY': JWT_SIGNING_KEY,
}

