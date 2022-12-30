from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
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

    # def clean_first_section(self):
    #     first_section = self.cleaned_data.get('first_section', [])
    #     if len(first_section) != 1:
    #         raise ValidationError(
    #             _('There can be only one Content Block in First Section'),
    #         )
    #     return self.cleaned_data.get('first_section')


class FinalAboutContentBlockAdmin(admin.ModelAdmin):
    form = FinalAboutContentBlockForm


admin.site.register(FinalAboutContentBlock, FinalAboutContentBlockAdmin)
admin.site.register(FirstSectionAboutContentBlock)
admin.site.register(HomeContentBlock)
admin.site.register(SecondSectionAboutContentBlock)
