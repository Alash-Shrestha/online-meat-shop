from django.contrib import admin
from recipe.models import *

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)