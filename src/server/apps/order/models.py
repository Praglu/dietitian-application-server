import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.offer.models import Offer
from server.apps.order.validators import ProductsJsonValidator
from server.apps.user.models import BonusUser


def default_products_with_quantity():
    return [
        {
            'id': 1,
            'quantity': 1,
        },
        {
            'id': 2,
            'quantity': 1,
        },
    ]


class Order(models.Model):
    uuid = models.UUIDField(null=True, unique=True, editable=False)
    user = models.ForeignKey(
        BonusUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    street = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    house_number = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )
    post_code = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    are_service_terms_accepted = models.BooleanField(default=False)
    date_of_order = models.DateTimeField(null=True, blank=True)
    products = models.ManyToManyField(Offer)
    products_with_quantity = models.JSONField(
        default=default_products_with_quantity,
        null=True,
        blank=True,
        help_text=_('id is your product id and quantity is how much of this product you want to buy'),
        validators=[
            ProductsJsonValidator,
        ],
    )
    sum = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        help_text=_('Sum will appear after saving this object')
    )
    additional_info = models.CharField(
        max_length=512,
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.user:  
            return f'Order {self.pk} made by {self.user.user.email}'
        return f'Order {self.pk} made by anon {self.email}'
