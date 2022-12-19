from django.urls import include, path

from rest_framework.routers import DefaultRouter

from server.apps.offer.views.offer import OfferViewSet

router = DefaultRouter()
router.register(r'', OfferViewSet, basename='offer')

urlpatterns = [
    path('', include(router.urls)),
]
