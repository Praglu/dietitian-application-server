import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.timezone import now


def file_storage_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(
        settings.FILE_UPLOAD_PATH,
        f'blogs/{uuid.uuid4()}.{ext}',
    )


class Blog(models.Model):
    title = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    date = models.DateField(
        default=now,
        editable=True,
        blank=True,
        null=True,
    )
    content_1 = models.CharField(
        max_length=512,
        blank=True,
        null=True,
    )
    content_2 = models.CharField(
        max_length=512,
        blank=True,
        null=True,
    )
    img = models.FileField(
        upload_to=file_storage_path,
        null=True,
        blank=True,
    )
    content_img = models.FileField(
        upload_to=file_storage_path,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.pk}_{self.title[:20]}'
