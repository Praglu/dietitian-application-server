from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = []

if settings.ADMIN_ENABLED:
    urlpatterns += [
        path(settings.ADMIN_ROOT_URL, admin.site.urls),
    ]
