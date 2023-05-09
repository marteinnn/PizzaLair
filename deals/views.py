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
