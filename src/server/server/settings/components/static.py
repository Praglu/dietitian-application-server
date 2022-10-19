import os

from server.settings.components.common import BASE_DIR

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'server', 'apps', 'admin', 'static'),
]
