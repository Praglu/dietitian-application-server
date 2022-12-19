from django.db import models

from server.apps.common.validators import OnlyDigitsValidator


class ContactForm(models.Model):
    first_and_last_name = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        validators=[
            OnlyDigitsValidator,
        ],
    )
    message = models.CharField(
        max_length=1024,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.pk} - {self.first_and_last_name}...'
