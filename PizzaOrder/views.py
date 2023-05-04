from django.shortcuts import render
from menu.models import Pizza
# Create your views here.
def order(request):
    return render(request, 'order/index.html', {
        'pizzas': Pizza.objects.all()
    })
