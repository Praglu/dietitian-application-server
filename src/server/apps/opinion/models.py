from django.db import models


class Opinion(models.Model):
    user_name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    opinion_text = models.CharField(
        max_length=512,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.pk} - {self.opinion_text[:15]}...'
