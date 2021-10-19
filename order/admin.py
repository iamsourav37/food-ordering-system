from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "food_details", "user", "status", "created_at")


admin.site.register(Order, OrderAdmin)

