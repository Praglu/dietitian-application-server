from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from server.apps.blog.models import Post
from server.apps.blog.serializers import PostSerializer
from server.apps.common.helpers_exception import exception_schema_dict


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Post.objects.all()

    @extend_schema(
        responses={
            200: PostSerializer,
            401: exception_schema_dict(
                (
                    NotAuthenticated,
                ),
            ),
            403: exception_schema_dict(
                (
                    PermissionDenied,
                ),
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
