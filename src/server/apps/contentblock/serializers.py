from rest_framework import serializers

from server.apps.contentblock.models import (
    FinalAboutContentBlock,
    FirstSectionAboutContentBlock,
    HomeContentBlock,
    SecondSectionAboutContentBlock,
)


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


class FirstSectionAboutContentBlockSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = FirstSectionAboutContentBlock
        fields = [
            'id',
            'img',
            'title',
            'content_1',
            'content_2',
        ]
        read_only_fields = fields


class SecondSectionAboutContentBlockSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = SecondSectionAboutContentBlock
        fields = [
            'id',
            'img',
            'content',
            'button_text',
            'button_link',
        ]
        read_only_fields = fields


class AboutContentBlockSerializer(serializers.ModelSerializer):
    first_section = FirstSectionAboutContentBlockSerializer()
    second_section = SecondSectionAboutContentBlockSerializer(many=True)
    class Meta(object):
        model = FinalAboutContentBlock
        fields = [
            'first_section',
            'second_section',
        ]
        read_only_fields = fields
