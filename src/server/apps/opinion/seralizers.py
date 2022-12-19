from rest_framework import serializers

from server.apps.opinion.models import Opinion


class OpinionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Opinion
        fields = [
            'id',
            'user_name',
            'opinion_text',
        ]
        read_only_fields = fields
