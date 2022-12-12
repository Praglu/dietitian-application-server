from django.urls import include, path

from rest_framework.routers import DefaultRouter

from server.apps.blog.views.blog import BlogViewSet

router = DefaultRouter()
router.register(r'', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
