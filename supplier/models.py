from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Supplier'
    
    def __str__(self):
        return self.user.username