from django.urls import path
from recipe.views import *

app_name = "recipe"
urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('item/<str:name>/', recipe, name='recipe'),
    path('search_recipe/', search_recipe, name='search_recipe'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('my_recipe/', my_recipe, name='my_recipe'),
]

