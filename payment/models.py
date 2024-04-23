from django.db import models
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    shipping_full_name = models.CharField(max_length=200, blank=True)
    shipping_email = models.EmailField(max_length=200, blank=True)
    shipping_address = models.CharField(max_length=200, null=True)
    shipping_city = models.CharField(max_length=200, null=True)
    shipping_state = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'ShippingAddress'

    def __str__(self):
        return f'Shipping Address - {str(self.id)}'


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    full_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    shipping_address = models.CharField(max_length=200, null=True)
    amount_paid = models.FloatField(max_length=10)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    shipping_address = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name_plural = 'Order'
    
    def __str__(self):
        return f'Order - {str(self.id)}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    quantity = models.IntegerField(default=1)
    price = models.FloatField(max_length=7)
    
    class Meta:
        verbose_name_plural = 'OrderItem'

    def __str__(self):
        return f'Order Item - {str(self.id)}'