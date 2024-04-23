from django.db import models
from users.models import User
# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Recipe'
        
    def __str__(self):
        return self.name