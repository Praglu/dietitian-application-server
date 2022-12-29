from rest_framework import serializers

from server.apps.contentblock.models import FinalAboutContentBlock, HomeContentBlock


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
    first_section_details = serializers.ReadOnlyField(source='first_section.values')
    second_section_details = serializers.ReadOnlyField(source='second_section.values')
    class Meta(object):
        model = FinalAboutContentBlock
        fields = [
            'first_section_details',
            'second_section_details',
        ]
        read_only_fields = fields
