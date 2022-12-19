import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.blog.models import Post


CONTENT_BLOCK_BUTTON_TEXTS = (
    (None, '---------'),
    ('Sprawdź ofertę', 'Sprawdź ofertę'),
    ('Dowiedz się więcej', 'Dowiedz się więcej'),
)


def file_storage_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(
        settings.FILE_UPLOAD_PATH,
        f'contentblocks/{uuid.uuid4()}.{ext}',
    )


class HomeContentBlock(models.Model):
    img = models.FileField(
        upload_to=file_storage_path,
        null=True,
        blank=True,
    )
    content = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    button_text = models.CharField(
        max_length=32,
        choices=CONTENT_BLOCK_BUTTON_TEXTS,
        default=CONTENT_BLOCK_BUTTON_TEXTS[0]
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    button_link = models.CharField(
        max_length=128,
        default='http://localhost:8002/api/offer',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.pk} - {self.content[:30]}...'


class AboutContentBlock(models.Model):
    img = models.FileField(
        upload_to=file_storage_path,
        null=True,
        blank=True,
    )
    content = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    button_text = models.CharField(
        max_length=32,
        choices=CONTENT_BLOCK_BUTTON_TEXTS,
        default=CONTENT_BLOCK_BUTTON_TEXTS[0]
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    button_link = models.CharField(
        max_length=128,
        default='http://localhost:8002/api/offer',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.pk} - {self.content[:30]}...'
