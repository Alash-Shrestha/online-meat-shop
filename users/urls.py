from django.urls import path

from users.views import login_page

app_name = "users"
urlpatterns = [
    path('', login_page, name='login'),
]
