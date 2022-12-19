from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

from server.apps.contentblock.models import AboutContentBlock, HomeContentBlock
from server.apps.contentblock.serializers import AboutContentBlockSerializer, HomeContentBlockSerializer
from server.apps.common.helpers_exception import exception_schema_dict


class HomeContentBlockViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HomeContentBlockSerializer
    permission_classes = ()

    def get_queryset(self):
        return HomeContentBlock.objects.all()

    @extend_schema(
        responses={
            200: HomeContentBlockSerializer,
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


class AboutContentBlockViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AboutContentBlockSerializer
    permission_classes = ()

    def get_queryset(self):
        return AboutContentBlock.objects.all()

    @extend_schema(
        responses={
            200: AboutContentBlockSerializer,
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