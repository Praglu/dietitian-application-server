import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.offer.models import Offer
from server.apps.order.validators import ProductsJsonValidator
from server.apps.user.models import BonusUser


PAYMENT_METHOD_CHOICES = (
    ('', '------'),
    ('Przelew tradycyjny', 'Przelew tradycyjny'),
)


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


class ProductWithQuantity(models.Model):
    offer = models.ForeignKey(
        Offer,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=True,
    )
    quantity = models.IntegerField(default=1, blank=False, null=True)

    def __str__(self):
        return f'{self.offer.title}  x{self.quantity}'


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
    products = models.ManyToManyField(ProductWithQuantity)
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
    payment_method = models.CharField(
        max_length=128,
        choices=PAYMENT_METHOD_CHOICES,
        null=True,
        blank=True,
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
