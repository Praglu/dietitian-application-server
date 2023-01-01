from rest_framework import serializers

from server.apps.offer.serializers import OfferSerializer
from server.apps.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    products = OfferSerializer(many=True)
    class Meta(object):
        model = Order
        fields = [
            'id',
            'products_with_quantity',
            'products',
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
            'sum',
        ]
        read_only_fields = fields
