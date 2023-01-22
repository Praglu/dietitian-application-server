from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from server.apps.contentblock.models import (
    FinalAboutContentBlock,
    FirstSectionAboutContentBlock,
    HomeContentBlock,
    SecondSectionAboutContentBlock,
)


class HomeContentBlockAdminForm(ModelForm):
    class Meta(object):
        model = HomeContentBlock
        fields = '__all__'
        widgets = {
            'content': AdminTextareaWidget
        }


class HomeContentBlockAdmin(admin.ModelAdmin):
    form = HomeContentBlockAdminForm


class FirstSectionContentBlockAdminForm(ModelForm):
    class Meta(object):
        model = FirstSectionAboutContentBlock
        fields = '__all__'
        widgets = {
            'content_1': AdminTextareaWidget,
            'content_2': AdminTextareaWidget,
        }


class FirstSectionContentBlockAdmin(admin.ModelAdmin):
    form = FirstSectionContentBlockAdminForm


class SecondSectionContentBlockAdminForm(ModelForm):
    class Meta(object):
        model = SecondSectionAboutContentBlock
        fields = '__all__'
        widgets = {
            'content': AdminTextareaWidget
        }


class SecondSectionContentBlockAdmin(admin.ModelAdmin):
    form = SecondSectionContentBlockAdminForm


class FinalAboutContentBlockForm(ModelForm):
    class Meta(object):
        model = FinalAboutContentBlock
        fields = '__all__'


class FinalAboutContentBlockAdmin(admin.ModelAdmin):
    form = FinalAboutContentBlockForm


admin.site.register(FinalAboutContentBlock, FinalAboutContentBlockAdmin)
admin.site.register(FirstSectionAboutContentBlock, FirstSectionContentBlockAdmin)
admin.site.register(HomeContentBlock, HomeContentBlockAdmin)
admin.site.register(SecondSectionAboutContentBlock, SecondSectionContentBlockAdmin)
