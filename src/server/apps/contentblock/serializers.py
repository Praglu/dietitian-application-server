from rest_framework import serializers

from server.apps.contentblock.models import AboutContentBlock, HomeContentBlock


class HomeContentBlockSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = HomeContentBlock
        fields = [
            'id',
            'img',
            'content',
            'button_text',
            'post',
            'button_link'
        ]
        read_only_fields = fields


class AboutContentBlockSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AboutContentBlock
        fields = [
            'id',
            'img',
            'content',
            'button_text',
            'post',
            'button_link'
        ]
        read_only_fields = fields
