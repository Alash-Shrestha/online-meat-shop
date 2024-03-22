from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from users.models import *

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are Logged In')
            return redirect('products:home')
        else:
            messages.success(request, 'Invalid username or password')
            return redirect('users:login_page')
    return render(request, 'users/login.html')

def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('products:login')
    return render(request, 'users/signup.html')

@login_required
def logout_page(request):
    logout(request)
    messages.success(request, 'You are Logged out')
    return redirect('users:login_page')