from django.shortcuts import render
from products.models import *

# Create your views here.
def home(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, 'products/home.html', context=context)

def product(request, name):
    product = Product.objects.get(name=name)
    context = {"product": product}
    return render(request, 'products/product.html', context=context)