from django.contrib import admin
from .models import Carts,Orders

@admin.register(Carts)
class CartsAdmin(admin.ModelAdmin):
    list_display = ['user','payment_date','payment_status']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['cart','title','payment_date','payment_status']


