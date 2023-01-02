from rest_framework import serializers

from server.apps.offer.serializers import OfferSerializer
from server.apps.order.models import Order, ProductWithQuantity


class ProductWithQuantitySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='offer.id')
    img = serializers.FileField(source='offer.img')
    title = serializers.ReadOnlyField(source='offer.title')
    short_description = serializers.ReadOnlyField(source='offer.short_description')
    full_description = serializers.ReadOnlyField(source='offer.full_description')
    amount = serializers.ReadOnlyField(source='offer.amount')

    class Meta(object):
        model = ProductWithQuantity
        fields = [
            'id',
            'img',
            'title',
            'short_description',
            'full_description',
            'amount',
            'quantity',
        ]
        read_only_fields = fields


class OrderSerializer(serializers.ModelSerializer):
    products = ProductWithQuantitySerializer(many=True)
    class Meta(object):
        model = Order
        fields = [
            'id',
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
