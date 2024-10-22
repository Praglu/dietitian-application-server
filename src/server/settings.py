import os
from pathlib import PurePath

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = PurePath(__file__).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv('DEBUG', 0))
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

if cors_allowed_origins := os.getenv('CORS_ALLOWED_ORIGINS'):
    CORS_ALLOWED_ORIGINS = cors_allowed_origins.split()

if cors_origin_whitelist := os.getenv('CORS_ORIGIN_WHITELIST'):
    CORS_ORIGIN_WHITELIST = cors_origin_whitelist.split()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd part
    'corsheaders',
    'drf_spectacular',
    'rest_framework',
    'rest_framework.authtoken',
    # project apps
    'server.apps.blog',
    'server.apps.common',
    'server.apps.contactform',
    'server.apps.contentblock',
    'server.apps.offer',
    'server.apps.opinion',
    'server.apps.order',
    'server.apps.user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'server/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    },
}


JWT_SIGNING_KEY = os.getenv('JWT_SIGNING_KEY', '')
JWT_VERIFYING_KEY = os.getenv('JWT_VERIFYING_KEY', None)

JWT_TOKEN_TYPE = os.getenv('JWT_TOKEN_TYPE', 'Bearer')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'RS256')

ACCESS_TOKEN_EXPIRE_SECONDS = int(os.getenv('ACCESS_TOKEN_EXPIRE_SECONDS', 60 * 5))
REFRESH_TOKEN_EXPIRE_SECONDS = int(os.getenv('REFRESH_TOKEN_EXPIRE_SECONDS', 60 * 60 * 24 * 30))


REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '200/hour'
    },
    'EXCEPTION_HANDLER': 'server.apps.common.exceptions.custom_exception_handler',
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

MIN_PASSWORD_LENGTH = int(os.getenv('MIN_PASSWORD_LENGTH', 8))
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'server.apps.user.validators.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': MIN_PASSWORD_LENGTH,
        },
    },
    {
        'NAME': 'server.apps.user.validators.AtLeastOneUpperValidator',
    },
    {
        'NAME': 'server.apps.user.validators.AtLeastOneLowerValidator',
    },
    {
        'NAME': 'server.apps.user.validators.AtLeastOneDigitOrSpecialValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'file_upload/'

MEDIA_ROOT = ''

FILE_UPLOAD_PATH = os.getenv('FILE_UPLOAD_PATH', 'file_upload')

ADMIN_ENABLED = os.getenv('ADMIN_ENABLED', 0)
ADMIN_ROOT_URL = os.getenv('ADMIN_ROOT_URL', 'admin/')
SWAGGER_ENABLED = int(os.getenv('SWAGGER_ENABLED', 1))

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django_auth_adfs': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = os.getenv('EMAIL_PORT', '')
# only one can be set true
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', False)
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', False)

LANGUAGE_CODE = 'pl-pl'
USE_I18N = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
