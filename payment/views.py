from django.shortcuts import render

from cart.cart import Cart
import hmac
import hashlib
import base64


# Create your views here.
def payment_success(request):
    return render(request, "payment/payment_success.html")


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    cart_total = cart.cart_total()
    total = cart_total["total"]
    product_total = cart_total["product_total"]
    
    uuid = "ab14a8f2b02c3"
    secret_key = "8gBm/:&EnhH.1/q"
    money = 100
    data_to_sign = f"{money},{uuid},EPAYTEST"
    signature = genSha256(secret_key, data_to_sign)
    
    return render(
        request,
        "payment/checkout.html",
        {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": total,
            "product_total": product_total,
            # "signature": signature,
            # "uuid": uuid,
        },
    )


def genSha256(key, message):
    key = key.encode("utf-8")
    message = message.encode("utf-8")

    hmac_sha256 = hmac.new(key, message, hashlib.sha256)
    return base64.b64encode(hmac_sha256.digest()).decode()


