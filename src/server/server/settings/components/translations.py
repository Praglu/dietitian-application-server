import os

from server.settings.components.common import BASE_DIR

LANGUAGE_CODE = 'pl-pl'
USE_I18N = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
