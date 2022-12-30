import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.blog.models import Post


def file_storage_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join(
        settings.FILE_UPLOAD_PATH,
        f'contentblocks/{uuid.uuid4()}.{ext}',
    )


CONTENT_BLOCK_BUTTON_TEXT_CHOICES = (
    ('', '-------'),
    ('Sprawdź ofertę', 'Sprawdź ofertę'),
    ('Dowiedz się więcej', 'Dowiedz się więcej'),
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
        max_length=128,
        choices=CONTENT_BLOCK_BUTTON_TEXT_CHOICES,
        null=True,
        blank=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    button_link = models.CharField(
        max_length=128,
        default="",
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.post is not None:
            self.button_link = f'/blog/{self.post.pk}'
        else:
            self.button_link = f'/oferta'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk} - {self.content[:30]}...'


class FirstSectionAboutContentBlock(models.Model):
    img = models.FileField(
        upload_to=file_storage_path,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    content_1 = models.CharField(
        max_length=512,
        null=True,
        blank=True,
    )
    content_2 = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.pk} - {self.content_1[:30]}...'


class SecondSectionAboutContentBlock(models.Model):
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
        max_length=128,
        choices=CONTENT_BLOCK_BUTTON_TEXT_CHOICES,
        null=True,
        blank=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    button_link = models.CharField(
        max_length=128,
        default="",
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.post is not None:
            self.button_link = f'/blog/{self.post.pk}'
        else:
            self.button_link = f'/oferta'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk} - {self.content[:30]}...'


class FinalAboutContentBlock(models.Model):
    first_section = models.ForeignKey(
        FirstSectionAboutContentBlock,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    second_section = models.ManyToManyField(SecondSectionAboutContentBlock)

    def __str__(self):
        return f'Content blocks with ID: {self.pk}'
