from django.http import JsonResponse
from django.shortcuts import render
from deals.models import Deals
from menu.models import Pizza
# Create your views here.
def deals(request):
    return render(request, 'deals/index.html', {
        'alldeals': Deals.objects.all()
    })

def twoforone(request):
    pizzas = Pizza.objects.all()
    return render(request, 'deals/two-for-one.html', {'pizzas': pizzas} )

def family(request):
    pizzas = Pizza.objects.all()
    return render(request, 'deals/family.html', {'pizzas': pizzas} )

def pizzaofmonth(request):
    pizzas = []
    for pizza in Pizza.objects.filter(name__icontains="diablo"):
        pizza_dict = {'id': pizza.PID, 'name': pizza.name, 'price': pizza.price / 2,
                      'description': pizza.description,
                      }
        pizzas.append(pizza_dict)
    return render(request, 'deals/pizzaofmonth.html', {'pizzas': pizza_dict} )


