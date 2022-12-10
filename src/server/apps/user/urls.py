from django.urls import include, path

from rest_framework.routers import DefaultRouter

from server.apps.user.views.user import ApiUserRegistrationView, UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path(
        'registration',
        ApiUserRegistrationView.as_view({
            'post': 'register_user',
        }),
        name='user_registration',
    ),
    path('', include(router.urls)),
]
