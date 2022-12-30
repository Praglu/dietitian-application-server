import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.common.validators import OnlyDigitsValidator


def file_storage_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(
        settings.FILE_UPLOAD_PATH,
        f'offer/{uuid.uuid4()}.{ext}',
    )


class Offer(models.Model):
    img = models.FileField(
        upload_to=file_storage_path,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    short_description = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )
    full_description = models.CharField(
        max_length=512,
        blank=True,
        null=True,
    )
    amount = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            OnlyDigitsValidator,
        ],
    )

    @property
    def amount_with_currency(self):
        return f'{self.amount} PLN'

    def __str__(self):
        return f'id:{self.pk} - {self.title}...'
