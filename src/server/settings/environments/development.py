import os

from server.settings.components.common import BASE_DIR, MIDDLEWARE

ALLOWED_HOSTS = ('*',)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

