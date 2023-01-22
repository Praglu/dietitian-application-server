from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm

from server.apps.offer.models import Offer


class OfferAdminForm(ModelForm):
    class Meta(object):
        model = Offer
        fields = '__all__'
        widgets = {
            'full_description': AdminTextareaWidget,
        }


class OfferAdmin(admin.ModelAdmin):
    form = OfferAdminForm


admin.site.register(Offer, OfferAdmin)
