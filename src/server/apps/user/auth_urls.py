from django.urls import path

from server.apps.user.views.auth_token import ApiObtainAuthTokenView, ApiRemoveAuthTokenView

urlpatterns = [
    path('obtain-auth-token', ApiObtainAuthTokenView.as_view(), name='obtain_auth_token'),
    path('remove-auth-token', ApiRemoveAuthTokenView.as_view(), name='remove_auth_token'),
]
