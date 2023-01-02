from django.contrib import admin

from server.apps.order.models import Order, ProductWithQuantity

admin.site.register(Order)
admin.site.register(ProductWithQuantity)
