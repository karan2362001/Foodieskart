from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Supplier)
admin.site.register(models.Product)

admin.site.register(models.product_order)
admin.site.register(models.OrderItem)