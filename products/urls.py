from django.urls import path

from products.views import home

app_name = "products"
urlpatterns = [
    path('', home, name='home'),
]
