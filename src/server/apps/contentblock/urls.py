from django.urls import include, path

from rest_framework.routers import DefaultRouter

from server.apps.contentblock.views.contentblocks import AboutContentBlockViewSet, HomeContentBlockViewSet

router = DefaultRouter()
router.register(r'about', AboutContentBlockViewSet, basename='about_content_blocks')
router.register(r'home', HomeContentBlockViewSet, basename='home_content_blocks')

urlpatterns = [
    path('', include(router.urls)),
]
