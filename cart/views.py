from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, CartItemDeals
from menu.models import Pizza
from django.contrib.auth.decorators import login_required
@login_required
def add_to_cart(request, id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    pizza = get_object_or_404(Pizza, PID=id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza=pizza, name=pizza.name)
    cart.total_price += pizza.price #* cart_item.quantity
    cart.save()
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def add_deal_to_cart(request, pizza_id, pizza1_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    pizza = get_object_or_404(Pizza, PID=pizza_id)
    pizza1 = get_object_or_404(Pizza, PID=pizza1_id)
    cart_item, created = CartItemDeals.objects.get_or_create(cart=cart, pizza=pizza, pizza1=pizza1, name="Two for One")
    if pizza.price > pizza1.price:
        cart.total_price += pizza.price #* cart_item.quantity
    else:
        cart.total_price += pizza1.price #* cart_item.quantity
    cart.save()
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def add_pofmonth_to_cart(request, id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    pizza = get_object_or_404(Pizza, PID=id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza=pizza, name="Pizza of the month")
    cart.total_price += round(pizza.price/2) #* cart_item.quantity
    cart.save()
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart = get_object_or_404(Cart, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    if cart_item.name == "Pizza of the month":
        cart.total_price -= (cart_item.pizza.price/2) #* cart_item.quantity
    else:
        cart.total_price -= cart_item.pizza.price #* cart_item.quantity
    cart.save()
    return redirect('cart')

def remove_deal_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItemDeals, id=cart_item_id)
    cart = get_object_or_404(Cart, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    if cart_item.pizza.price > cart_item.pizza1.price:
        cart.total_price -= cart_item.pizza.price  # * cart_item.quantity
    else:
        cart.total_price -= cart_item.pizza1.price  # * cart_item.quantity
    cart.save()
    return redirect('cart')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    cart_deal_items = cart.cartitemdeals_set.all()
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'cart_item_deals': cart_deal_items, 'total_price': cart.total_price})

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')

def payment(request):
    return render(request, 'cart/payment.html')
