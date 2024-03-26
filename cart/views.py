from django.shortcuts import render, get_object_or_404
from cart.cart import Cart
from products.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_view(request):
    return render(request, 'cart/cart.html')

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        # Look product in DB
        product = get_object_or_404(Product, id=product_id)
        # Save to session
        cart.add(product=product)
        response = JsonResponse({'Product Name ': product.name})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass