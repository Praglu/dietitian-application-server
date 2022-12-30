from rest_framework import serializers

from server.apps.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Order
        fields = [
            'first_name',
            'last_name',
            'street',
            'house_number',
            'post_code',
            'city',
            'email',
            'phone',
            'are_service_terms_accepted',
            'additional_info',
            'products_with_quantity',
            'sum',
        ]
        read_only_fields = fields
