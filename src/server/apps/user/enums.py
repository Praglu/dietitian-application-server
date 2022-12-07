from enum import Enum

from django.utils.translation import gettext as _


class UserGroup(Enum):
    CUSTOMER = 'customer'
    MANAGER = 'manager'


group_translations = (
    _('customer'),
    _('manager'),
)
