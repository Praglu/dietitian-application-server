from rest_framework import permissions

from server.apps.common.helpers_auth import belongs_to_group
from server.apps.user.enums import UserGroup


class IsCustomerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return belongs_to_group(request, UserGroup.CUSTOMER.value)
