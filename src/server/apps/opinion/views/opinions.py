from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from server.apps.common.helpers_exception import exception_schema_dict
from server.apps.opinion.models import Opinion
from server.apps.opinion.seralizers import OpinionSerializer


class OpinionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OpinionSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Opinion.objects.all()

    @extend_schema(
        responses={
            200: OpinionSerializer,
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
