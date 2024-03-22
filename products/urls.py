from django.urls import path

from products.views import home, product

app_name = "products"
urlpatterns = [
    path('', home, name='home'),
    path('product/<str:name>/', product, name='product'),
]
