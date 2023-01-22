from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import ModelForm

from server.apps.blog.models import Post


class PostAdminform(ModelForm):
    class Meta(object):
        model = Post
        fields = '__all__'
        widgets = {
            'content_1': AdminTextareaWidget,
            'content_2': AdminTextareaWidget,
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminform


admin.site.register(Post, PostAdmin)
