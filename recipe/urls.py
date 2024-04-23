from django.urls import path
from recipe.views import *

app_name = "recipe"
urlpatterns = [
    path('', recipe_list, name='recipe_list'),
]

