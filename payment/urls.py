from django.urls import path
from payment.views import *

app_name = "payment"
urlpatterns = [
    path('payment_success/', payment_success, name='payment_success'),
    path('checkout', checkout, name='checkout'),
]
