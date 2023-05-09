from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from menu.models import Pizza

def add_to_cart(request, id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    pizza = get_object_or_404(Pizza, PID=id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza=pizza)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'cart/cart.html', {'cart_items': cart_items})
