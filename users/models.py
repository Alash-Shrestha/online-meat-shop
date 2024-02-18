from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name