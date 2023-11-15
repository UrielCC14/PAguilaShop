from django.contrib import admin
from .models import Category,Product,Sale,Zona,Tickets,Shipping_Address,Targets,Sale_Tickets

class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ("order_date")

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Zona)
admin.site.register(Tickets)
admin.site.register(Shipping_Address)
admin.site.register(Targets)
admin.site.register(Sale_Tickets)