from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('auth/', include('server.apps.user.auth_urls')),
    path('api/user/', include('server.apps.user.urls')),
    path('api/blog/', include('server.apps.blog.urls')),
    path('api/contact-form', include('server.apps.contactform.urls')),
    path('api/content-blocks/', include('server.apps.contentblock.urls')),
    path('api/offer/', include('server.apps.offer.urls')),
    path('api/opinions/', include('server.apps.opinion.urls')),
    path('api/order/', include('server.apps.order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.SWAGGER_ENABLED:
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]

if settings.ADMIN_ENABLED:
    urlpatterns += [
        path(settings.ADMIN_ROOT_URL, admin.site.urls),
    ]
