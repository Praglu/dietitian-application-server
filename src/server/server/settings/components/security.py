# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
import os

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_KEY = 'django-insecure-0^hbxm80u8xox((1ay(ly@mplnu-vjq(k+&8mevd0&ks@!2(fm'

MIN_PASSWORD_LENGTH = int(os.getenv('MIN_PASSWORD_LENGTH', 11))
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'server.settings.password_validators.minimum_length.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': MIN_PASSWORD_LENGTH,
        },
    },
    {
        'NAME': 'server.settings.password_validators.at_least_one_upper.AtLeastOneUpperValidator',
    },
    {
        'NAME': 'server.settings.password_validators.at_least_one_lower.AtLeastOneLowerValidator',
    },
    {
        'NAME': 'server.settings.password_validators.at_least_one_digit.AtLeastOneDigitValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_USER_MODEL = 'account.Account'
PASSWORD_EXPIRATION_DAYS = int(os.getenv('PASSWORD_EXPIRATION_DAYS', 60))

CSRF_TRUSTED_ORIGINS = ['']

SALT_SIZE = int(os.getenv('SALT_SIZE', 16))

# BLACKLISTED_USER_TEMPLATE = 'blacklisted_user:{user_id}'
# BLACKLIST_ALLOWED_PATHS_REGEX = {
#     '^/api/(?P<version>(v1))/account/employee/reset-password',
#     '^/api/(?P<version>(v1))/token',
# }
