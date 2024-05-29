from django.urls import path
from supplier.views import *

app_name = "supplier"
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_page, name='login_page'),
    path('deliver/', deliver, name='deliver'),
    path('history/', orders, name='orders'),
    path('products/', products, name='products'),
    path('logout/', logout_page, name='logout_page'),
    path('stock/', stock, name='stock'),
    path('update_profile', update_profile, name='update_profile'),
]