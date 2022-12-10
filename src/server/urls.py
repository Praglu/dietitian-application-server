from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('auth/', include('server.apps.user.auth_urls')),
    path('api/user/', include('server.apps.user.urls')),
]

if settings.SWAGGER_ENABLED:
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]

if settings.ADMIN_ENABLED:
    urlpatterns += [
        path(settings.ADMIN_ROOT_URL, admin.site.urls),
    ]
