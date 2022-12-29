from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from server.apps.contentblock.models import FinalAboutContentBlock, HomeContentBlock
from server.apps.contentblock.serializers import AboutContentBlockSerializer, HomeContentBlockSerializer
from server.apps.common.helpers_exception import exception_schema_dict


class HomeContentBlockViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HomeContentBlockSerializer
    authentication_classes = ()
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
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        return FinalAboutContentBlock.objects.all()

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
