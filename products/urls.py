from django.urls import path

from products.views import *

app_name = "products"
urlpatterns = [
    path('', index, name='index'),
    path('product/<str:name>/', product, name='product'),
    path('category/<str:name>/', category, name='category'),
    path('search_product/', search_product, name='search_product'),
]
