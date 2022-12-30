from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class BonusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    street = models.CharField(max_length=128, null=True, blank=True)
    house_number = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    post_code = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f'Bonus data from user with id:{self.user.pk} - {self.user.email}'
