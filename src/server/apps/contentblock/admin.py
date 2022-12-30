from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from server.apps.contentblock.models import (
    FinalAboutContentBlock,
    FirstSectionAboutContentBlock,
    HomeContentBlock,
    SecondSectionAboutContentBlock,
)


class FinalAboutContentBlockForm(forms.ModelForm):
    class Meta(object):
        model = FinalAboutContentBlock
        fields = '__all__'


class FinalAboutContentBlockAdmin(admin.ModelAdmin):
    form = FinalAboutContentBlockForm


admin.site.register(FinalAboutContentBlock, FinalAboutContentBlockAdmin)
admin.site.register(FirstSectionAboutContentBlock)
admin.site.register(HomeContentBlock)
admin.site.register(SecondSectionAboutContentBlock)
