from rest_framework import serializers

from server.apps.blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Post
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
