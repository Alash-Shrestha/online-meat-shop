from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from supplier.models import *
from payment.models import *


# Create your views here.
def index(request):
    order = Order.objects.all()
    order_item = OrderItem.objects.all()
    return render(
        request, "supplier/order.html", {"orders": order, "order_items": order_item}
    )


def deliver(request):
    if request.method=="POST":
        order_id = request.POST.get("order_id")
        print(order_id)
        order = Order.objects.get(id=order_id)
        order.complete = 1
        order.save()
        return redirect("supplier:index")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are Logged In")
            return redirect("supplier:index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("supplier:login_page")
    return render(request, "supplier/login.html")

def orders(request):
    orders = Order.objects.all()
    order_items = OrderItem.objects.all()
    return render(request, "supplier/order_list.html", {"orders": orders, "order_items": order_items})


def logout_page(request):
    logout(request)
    return redirect("supplier:login_page")


def products(request):
    products = Product.objects.all()
    return render(request, "supplier/products.html", {"products": products})

def stock(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        stock = request.POST.get("stock")
        product = Product.objects.get(id=product_id)
        if stock == "1":
            product.stock = True
            product.save()
        else:
            product.stock = False
            product.save()
        return redirect("supplier:products")
    pass


def update_profile(request):
    return render(request, "supplier/update_profile.html")