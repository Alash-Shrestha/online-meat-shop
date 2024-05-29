from django.shortcuts import render, redirect
from django.contrib import messages
from cart.cart import Cart
import uuid
import requests
import json

from payment.models import Order, OrderItem


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    cart_total = cart.cart_total()
    totals = cart_total["total"]
    product_total = cart_total["product_total"]
    uid = uuid.uuid4()
    return render(
        request,
        "payment/checkout.html",
        {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "product_total": product_total,
            "uid": uid,
        },
    )


def process_order(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            cart = Cart(request)
            cart_products = cart.get_prods()
            quantities = cart.get_quants()
            totals = cart.cart_total()["total"]
            full_name = request.POST.get("full_name")
            email = request.POST.get("email")
            shipping_address = request.POST.get("shipping_address")

            create_order = Order.objects.create(
                user=request.user,
                full_name=full_name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=totals,
            )
            create_order.save()
            order_id = create_order.pk
            print(cart_products)
            for product in cart_products:
                product_id = product.id
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                quantity = quantities.get(str(product_id), 0)
                create_order_item = OrderItem.objects.create(
                    order_id=order_id,
                    product_id=product_id,
                    user=user,
                    quantity=quantity,
                    price=price,
                )
                create_order_item.save()
            for key in list(request.session.keys()):
                if key == "session_key":
                    # Delete the key
                    del request.session[key]
            messages.success(request, "Order Placed Successfully")
            return redirect("products:index")
    else:
        return redirect("payment:checkout")


def khalti(request):
    url = "https://a.khalti.com/api/v2/epayment/initiate/"

    return_url = request.POST.get("return_url")
    purchase_order_id = request.POST.get("purchase_order_id")
    amount = request.POST.get("amount")
    user = request.user
    name = user.username if user.username else "test"
    email = user.email if user.email else "test@gmail.com"

    payload = json.dumps(
        {
            "return_url": return_url,
            "website_url": return_url,
            "amount": amount,
            "purchase_order_id": purchase_order_id,
            "purchase_order_name": "test",
            "customer_info": {
                "name": name,
                "email": email,
                "phone": "9800000001",
            },
        }
    )
    headers = {
        "Authorization": "key 88f3bff111b243b7ac9ee1214b013001",
        "Content-Type": "application/json",
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)

        new_response = json.loads(response.text)
        return redirect(new_response["payment_url"])
    except:
        messages.error(request, "Payment failed")
        return redirect("payment:checkout")


def verifyKhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/lookup/"
    if request.method == "GET":
        headers = {
            "Authorization": "key 88f3bff111b243b7ac9ee1214b013001",
            "Content-Type": "application/json",
        }
        pidx = request.GET.get("pidx")
        data = json.dumps({"pidx": pidx})
        response = requests.request("POST", url, headers=headers, data=data)
        new_resposne = json.loads(response.text)

        if new_resposne["status"] == "Completed":
            messages.success(request, "Payment successful")
            process_order(request)
        else:
            messages.error(request, "Payment failed")
        return redirect("products:index")

