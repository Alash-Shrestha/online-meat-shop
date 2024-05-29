from django.db import models
from users.models import User
from products.models import Category
# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name_plural = 'Ingredient'
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="recipe/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    instructions = models.TextField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Recipe'
        
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = "https://imgs.search.brave.com/oB6fgT45DC10B0RQfk3kTBtZ0W-2p7udZUxPnfvKT3M/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzA0LzYyLzkzLzY2/LzM2MF9GXzQ2Mjkz/NjY4OV9CcEVFY3hm/Z011WVBmVGFJQU9D/MXRDRHVybXNubzdT/cC5qcGc"
        return url