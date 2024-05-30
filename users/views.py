from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from payment.models import Order, OrderItem
from users.models import *
import json
import re
from cart.cart import Cart


# Create your views here.
def validate_password(password):
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    if re.match(pattern, password):
        return True
    else:
        return False


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = Customer.objects.get(user=request.user)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)
            messages.success(request, f"Welcome {user.username}")
            return redirect("products:index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("users:login_page")
    return render(request, "users/login.html")


def signup_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if validate_password(password):
            if password == confirm_password:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                customer = Customer(user=user, phone=phone)
                customer.save()
                return redirect("users:login_page")
            else:
                messages.error(request, "Password do not match",)
            return redirect("users:signup_page")
        else:
            messages.error(request, "Password must contain at least 8 characters with numeric value")
            return redirect("users:signup_page")
    return render(request, "users/signup.html")


@login_required
def logout_page(request):
    logout(request)
    messages.success(request, "You are Logged out")
    return redirect("users:login_page")


@login_required
def update_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        user = request.user
        user_changed = False
        if username != user.username or email != user.email:
            user.username = username
            user.email = email
            user.save()
            user_changed = True

        current_customer = Customer.objects.get(user=user)
        if phone != current_customer.phone:
            current_customer.phone = phone
            current_customer.save()
            user_changed = True
        if user_changed:
            messages.success(request, "Profile Updated")
        else:
            messages.success(request, "No Changes Made")
        return redirect("users:update_user")
    else:
        current_user = Customer.objects.get(user=request.user)
        return render(
            request,
            "users/update_user.html",
            {"current_user": current_user},
        )


def upload_image(request):
    if request.method == "POST" and "image" in request.FILES:
        image = request.FILES["image"]
        customer = Customer.objects.get(user=request.user)
        customer.image = image
        customer.save()
        messages.success(request, "Image uploaded successfully")
        return redirect("users:update_user")
    else:
        messages.error(request, "Error uploading image")
        return redirect("users:update_user")

def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        user = request.user
        if user.check_password(old_password):
            if validate_password(new_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, "Password changed successfully")
                    return redirect("users:update_user")
                else:
                    messages.error(request, "Passwords do not match")
                    return redirect("users:update_user")
            else:
                messages.error(request, "Password must contain at least 8 characters with numeric value")
                return redirect("users:update_user")
        else:
            messages.error(request, "Invalid old password")
            return redirect("users:update_user")
    else:
        return redirect("users:update_user")


def order(request):
    orders = Order.objects.filter(user=request.user)
    order_items = OrderItem.objects.filter(user=request.user)
    return render(
        request, "users/order.html", {"orders": orders, "order_items": order_items}
    )


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def check_email(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            user_id = user.id
            return redirect("users:forgot_password", id=user_id)
        except User.DoesNotExist:
            messages.error(request, "Email does not exist")
            return redirect("users:check_email")
    else:
        return render(request, "users/check_email.html")


def forgot_password(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if validate_password(password):
            if password == confirm_password:
                user.set_password(password)
                user.save()
                messages.success(request, "Password changed successfully")
                return redirect("users:login_page")
            else:
                messages.error(request, "Passwords do not match")
                return redirect("users:forgot_password", id=id)
        else:
            messages.error(
                request,
                "Password must contain at least 8 characters with numeric value",
            )
            return redirect("users:forgot_password", id=id)
    else:
        return render(request, "users/forgot_password.html")
