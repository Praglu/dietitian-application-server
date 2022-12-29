from django.contrib import admin

from server.apps.user.models import BonusUser


class BonusInline(admin.StackedInline):
    model = BonusUser
    can_delete = False
    fk_name = 'user'


class CustomUserAdmin(admin.StackedInline):
    inlines = ('BonusInline',)


class BonusUserAdmin(admin.ModelAdmin):
    model = BonusUser
    # fields = ('__all__',)

admin.site.register(BonusUser, BonusUserAdmin)
