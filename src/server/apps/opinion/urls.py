from django.urls import include, path

from rest_framework.routers import DefaultRouter

from server.apps.opinion.views.opinions import OpinionViewSet

router = DefaultRouter()
router.register(r'', OpinionViewSet, basename='opinions')

urlpatterns = [
    path('', include(router.urls)),
]
