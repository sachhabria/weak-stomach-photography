from django.shortcuts import render, redirect, get_object_or_404

from store.models import Variant
from .cart import Cart

# Create your views here.

CART_SESSION_ID = 'cart'

def detail(request):
    cart = Cart(request)
    subtotal = sum(float(item['price']) * item['quantity'] for item in cart)
    return render(request, 'cart/detail.html', { 'cart': cart, 'subtotal': subtotal })

def add_to_cart(request):
    """
    Retrieve the user's cart from the session, or create a new one 
    and add the selected item to the cart.
    """
    variant = get_object_or_404(Variant, id=request.POST["variant"])
    cart = Cart(request)
    cart.add(variant, int(request.POST["quantity"]))
    return redirect('cart:detail')

def remove_from_cart(request, variant_id):
    variant = get_object_or_404(Variant, id=variant_id)
    cart = Cart(request)
    cart.remove(variant)
    return redirect('cart:detail')