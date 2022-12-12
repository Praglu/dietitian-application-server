import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.blog.models import Blog


CONTENT_BLOCK_BUTTON_TEXTS = (
    (_('Check offer'), _('Check offer')),
    (_('Find out more'), _('Find out more')),
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
    blog = models.ForeignKey(
        Blog,
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
        return f'{self.pk}_{self.content[:30]}'
