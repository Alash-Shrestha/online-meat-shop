from django.contrib import admin
from payment.models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(ShippingAddress)
# admin.site.register(Order)
admin.site.register(OrderItem)

# Create OrderItem Inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

# Extend Order Model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)