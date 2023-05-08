from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def cart(request):
    context = {}
    return render(request, "cart/cart.html", context)

def add_to_cart(request):
    return JsonResponse("Working", safe=False)