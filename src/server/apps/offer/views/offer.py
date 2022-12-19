from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

from server.apps.offer.models import Offer
from server.apps.offer.serializers import OfferSerializer
from server.apps.common.helpers_exception import exception_schema_dict


class OfferViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OfferSerializer
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        return Offer.objects.all()

    @extend_schema(
        responses={
            200: OfferSerializer,
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
