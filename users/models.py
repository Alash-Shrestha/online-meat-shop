from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to="customer/", null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name_plural = 'Customer'
    
    def __str__(self):
        return self.user.username
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = None
        return url