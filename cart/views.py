from django.shortcuts import render, get_object_or_404
from cart.cart import Cart
from products.models import Product
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
def cart_view(request):
    # Get the cart
    if request.method == "POST":
        searchData = request.POST.get("search_product")
        if searchData != "":
            products = Product.objects.filter(name__icontains=searchData)
            if len(products) == 0:
                messages.warning(request, "Products Not Found")
            else:
                return render(request, "products/index.html", {"products": products})
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    cart_total = cart.cart_total()
    total = cart_total["total"]
    product_total = cart_total["product_total"]
    return render(
        request,
        "cart/cart.html",
        {"cart_products": cart_products, "quantities": quantities, "totals": total, "product_total": product_total},
    )


def cart_add(request):
    # Get the cart
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        # Look product in DB
        product = get_object_or_404(Product, id=product_id)
        # Save to session
        cart.add(product=product, quantity=product_qty)
        # Get Cart quantity
        cart_quantity = cart.__len__()
        # response = JsonResponse({'Product Name ': product.name})
        response = JsonResponse({"qty": cart_quantity})
        messages.success(request, "Product Added to Cart")
        return response


def cart_delete(request):
    # Get the cart
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        # Delete from session
        cart.delete(product=product_id)
        response = JsonResponse({"product": product_id})
        messages.success(request, "Product Deleted from Cart")
        return response

def cart_update(request):
    # Get the cart
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        # Update the session
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({"qty": product_qty})
        messages.success(request, "Cart Updated")
        return response
