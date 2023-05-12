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

@login_required
def add_deal_to_cart(request, typeofdeal ,pizza_id, pizza1_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    pizza = get_object_or_404(Pizza, PID=pizza_id)
    pizza1 = get_object_or_404(Pizza, PID=pizza1_id)
    if typeofdeal == 'twoforone':
        cart_item, created = CartItemDeals.objects.get_or_create(cart=cart, pizza=pizza, pizza1=pizza1, name="Two for One")
        if pizza.price > pizza1.price:
            cart.total_price += pizza.price #* cart_item.quantity
        else:
            cart.total_price += pizza1.price #* cart_item.quantity
    elif typeofdeal == 'family':
        cart_item, created = CartItemDeals.objects.get_or_create(cart=cart, pizza=pizza, pizza1=pizza1,
                                                                 name="Family order")
        cart.total_price += 40
    cart.save()
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
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
    if cart_item.name == "Pizza of the month":
        cart.total_price -= (cart_item.pizza.price/2) * cart_item.quantity
    else:
        cart.total_price -= cart_item.pizza.price * cart_item.quantity
    cart_item.delete()
    cart.save()
    return redirect('cart')

@login_required
def remove_deal_from_cart(request, typeofdeal, cart_item_id):
    cart_item = get_object_or_404(CartItemDeals, id=cart_item_id)
    cart = get_object_or_404(Cart, user=request.user)
    if typeofdeal == 'Two for One':
        if cart_item.pizza.price > cart_item.pizza1.price:
            cart.total_price -= cart_item.pizza.price * cart_item.quantity
        else:
            cart.total_price -= cart_item.pizza1.price * cart_item.quantity
    elif typeofdeal == 'Family order':
        cart.total_price -= 40 * cart_item.quantity
    cart_item.delete()
    cart.save()
    return redirect('cart')

@login_required
def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.delete()
    return redirect('cart')

@login_required
def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart = cart_item.cart
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    cart.total_price -= cart_item.pizza.price
    cart.save()
    return redirect('cart')

@login_required
def increase_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart = cart_item.cart
    cart_item.quantity += 1
    cart_item.save()
    if cart_item.name == "Pizza of the month":
        cart.total_price += cart_item.pizza.price / 2
    else:
        cart.total_price += cart_item.pizza.price
    cart.save()
    return redirect('cart')

@login_required
def decrease_deal_quantity(request, typeofdeal, item_id):
    cart_item = get_object_or_404(CartItemDeals, id=item_id)
    cart = cart_item.cart
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    if typeofdeal == 'Two for One':
        if cart_item.pizza.price > cart_item.pizza1.price:
            cart.total_price -= cart_item.pizza.price
        else:
            cart.total_price -= cart_item.pizza1.price
    elif typeofdeal == 'Family order':
        cart.total_price -= 40
    cart.save()
    return redirect('cart')

@login_required
def increase_deal_quantity(request, typeofdeal, item_id):
    cart_item = get_object_or_404(CartItemDeals, id=item_id)
    cart = cart_item.cart
    cart_item.quantity += 1
    cart_item.save()
    if typeofdeal == 'Two for One':
        if cart_item.pizza.price > cart_item.pizza1.price:
            cart.total_price += cart_item.pizza.price
        else:
            cart.total_price += cart_item.pizza1.price
    elif typeofdeal == 'Family order':
        cart.total_price += 40
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

@login_required
def payment(request):
    return render(request, 'cart/payment.html')

@login_required
def review(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    cart_deal_items = cart.cartitemdeals_set.all()
    return render(request, 'cart/review.html', {'cart_items': cart_items, 'cart_item_deals': cart_deal_items, 'total_price': cart.total_price})

@login_required
def pickpayment(request):
    return render(request, 'cart/pick-payment.html')

@login_required
def confirmation(request):
    return render(request, 'cart/confirmation.html')

@login_required
def clear_cart_and_redirect(request):
    clear_cart(request)
    return redirect('frontpage-index')