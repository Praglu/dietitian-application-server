from rest_framework import serializers

from server.apps.blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Blog
        fields = [
            'id',
            'img',
            'title',
            'date',
            'content_1',
            'content_2',
            'content_img',
        ]
        read_only_fields = fields
