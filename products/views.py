from django.shortcuts import render, redirect
from products.models import *
from django.contrib import messages
import random

# Create your views here.
def index(request):
    product = Product.objects.all()
    categories = Category.objects.all()
    return render(
        request, "products/index.html", {"products": product, "categories": categories}
    )


def product(request, name):
    product = Product.objects.get(name=name)
    related_products = Product.objects.all()
    related_products = list(related_products)
    related_products = random.sample(related_products, 4)
    return render(request, "products/product.html", {"product": product, "related_products": related_products})


def category(request, name):
    try:
        category = Category.objects.get(name=name)
        product = Product.objects.filter(category=category)
        categories = Category.objects.all()
        return render(
            request,
            "products/category.html",
            {"categories": categories, "products": product},
        )
    except:
        messages.error(request, "Invalid Category")
        return redirect("products:index")


def category_summary(request):
    categories = Category.objects.all()
    return render(request, "products/category_summary.html", {"categories": categories})


def search_product(request):
    if request.method == "POST":
        searchData = request.POST.get("search_product")
        if searchData != "":
            products = Product.objects.filter(name__icontains=searchData)
            if len(products) == 0:
                messages.warning(request, "Products Not Found")
                return redirect("products:index")
            else:
                return render(request, "products/search.html", {"products": products})