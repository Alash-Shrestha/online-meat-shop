from products.models import Product
from users.models import Customer


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request
        # Get the current session key if exists
        cart = self.session.get("session_key")
        # If the user is new, create a new session key
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}
        # Make cart available in all pages
        self.cart = cart


    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
        if self.request.user.is_authenticated:
            current_user = Customer.objects.filter(user=self.request.user)
            carty = str(self.cart)
            carty = carty.replace("\'", '\"')
            current_user.update(old_cart=str(carty)) 


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
        
        if self.request.user.is_authenticated:
            current_user = Customer.objects.filter(user=self.request.user)
            carty = str(self.cart)
            carty = carty.replace("\'", '\"')
            current_user.update(old_cart=str(carty))

    def cart_total(self):
        product_ids = self.cart.keys()
        # Search products with those keys in Product Database
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        product_total = {}
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.sale_price:
                        product_total[key] = product.sale_price * value
                        total += product.sale_price * value
                    else:
                        product_total[key] = product.price * value
                        total += product.price * value
        return {"total": total, "product_total": product_total}

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to view products in database
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        # Update Cart
        self.cart[product_id] = product_qty
        self.session.modified = True
        if self.request.user.is_authenticated:
                current_user = Customer.objects.filter(user=self.request.user)
                carty = str(self.cart)
                carty = carty.replace("\'", '\"')
                current_user.update(old_cart=str(carty))
        return self.cart
    
        

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        
        if self.request.user.is_authenticated:
            current_user = Customer.objects.filter(user=self.request.user)
            carty = str(self.cart)
            carty = carty.replace("\'", '\"')
            current_user.update(old_cart=str(carty))
