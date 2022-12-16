from django.contrib import admin

from server.apps.contentblock.models import AboutContentBlock, HomeContentBlock

admin.site.register(HomeContentBlock)
admin.site.register(AboutContentBlock)
