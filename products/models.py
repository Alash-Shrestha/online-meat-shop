from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=6)
    # price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField(max_length=250, default="", blank=True, null=True)
    image = models.ImageField(upload_to="product/", null=True, blank=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.FloatField(max_length=6, null=True, blank=True)
    stock = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = "https://imgs.search.brave.com/oB6fgT45DC10B0RQfk3kTBtZ0W-2p7udZUxPnfvKT3M/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzA0LzYyLzkzLzY2/LzM2MF9GXzQ2Mjkz/NjY4OV9CcEVFY3hm/Z011WVBmVGFJQU9D/MXRDRHVybXNubzdT/cC5qcGc"
        return url
