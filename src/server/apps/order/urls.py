from django.urls import include, path

from rest_framework.routers import DefaultRouter

from server.apps.order.views.orders import NewOrderView, OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'make-order',
        NewOrderView.as_view({
            'post': 'make_new_order',
        }),
        name='new_order',
    ),
]
