from rest_framework import serializers

from server.apps.offer.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Offer
        fields = [
            'id',
            'img',
            'title',
            'short_description',
            'full_description',
            'amount_with_currency'
        ]
        read_only_fields = fields
