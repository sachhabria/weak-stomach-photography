from store.models import Variant, Product

CART_SESSION_ID = 'cart'

class Cart(object):

    def __init__(self, request):
        """
        Fetch the session cart or create a new one if it doesn't exist.
        """
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Loop through cart items and fetch the products from the database.
        """
        for item in self.cart.values():
            yield item

    def add(self, variant, quantity):
        """
        Add a product to the cart and update its quantity.
        """
        variant_id = str(variant.id)
        if variant_id not in self.cart:
            self.cart[variant_id] = {
                'title': variant.product.title,
                'price': str(variant.price),
                'quantity': 0,
            }
        self.cart[variant_id]['quantity'] += quantity
        if self.cart[variant_id]['quantity'] == 0:
            self.remove(variant)
        self.save()
    
    def remove(self, variant):
        """
        Remove a product from the cart.
        """
        variant_id = str(variant.id)
        if variant_id in self.cart:
            del self.cart[variant_id]
            self.save()
    
    def save(self):
        """
        Update the session cart and mark the session as modified to make sure it is saved.
        """
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True
