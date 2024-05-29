from django.urls import path

from users.views import *

app_name = "users"
urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('signup/', signup_page, name='signup_page'),
    path('logout/', logout_page, name='logout_page'),
    path('update/', update_user, name='update_user'),
    path('upload_image', upload_image, name='upload_image'),
    path('change_password/', change_password, name='change_password'),
    path('order/', order, name='order'),
    path('about', about, name='about'),
]
