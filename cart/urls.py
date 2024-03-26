from django.urls import path

from cart.views import *

app_name = "cart"
urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/', cart_add, name='cart_add'),
    path('delete/', cart_delete, name='cart_delete'),
    path('update/', cart_delete, name='cart_update'),
]
