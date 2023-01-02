from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from server.apps.common.helpers_exception import exception_schema_dict
from server.apps.order.models import Order
from server.apps.order.serializers.order_get import OrderSerializer
from server.apps.order.serializers.order_post import OrderPayloadSerializer
from server.datastore.commands.new_order import MakeNewOrderCommand


class NewOrderView(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    @extend_schema(
        request=OrderPayloadSerializer,
        responses={
            204: None,
            401: exception_schema_dict(
                (
                    NotAuthenticated,
                ),
            ),
            403: exception_schema_dict(
                (
                    PermissionDenied,
                ),
            ),
        },
    )
    @action(
        detail=True,
        methods=['post'],
    )
    def make_new_order(self, request, **kwargs):
        payload_serializer = OrderPayloadSerializer(data=request.data)
        payload_serializer.is_valid(raise_exception=True)
        command = MakeNewOrderCommand(
            first_name=payload_serializer.data['first_name'],
            last_name=payload_serializer.data['last_name'],
            street=payload_serializer.data['street'],
            house_number=payload_serializer.data['house_number'],
            post_code=payload_serializer.data['post_code'],
            city=payload_serializer.data['city'],
            email=payload_serializer.data['email'],
            phone=payload_serializer.data['phone'],
            are_service_terms_accepted=payload_serializer.data['are_service_terms_accepted'],
            additional_info=payload_serializer.data['additional_info'],
            products=payload_serializer.data['products'],
            payment_method=payload_serializer.data['payment_method'],
            sum=payload_serializer.data['sum'],
        )
        command.make_new_order()

        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Order.objects.filter(user__user=self.request.user.id)

    @extend_schema(
        responses={
            200: OrderSerializer,
            401: exception_schema_dict(
                (
                    NotAuthenticated,
                ),
            ),
            403: exception_schema_dict(
                (
                    PermissionDenied,
                ),
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
