from django.shortcuts import render

pizzas = [
    {'name': 'Margarita', 'price': 1200},
    {'name': 'Pepperoni', 'price': 1600},
    {'name': 'Vegan', 'price': 1600},
]

# Create your views here.
def menu(request):
    return render(request, 'menu/index.html', context={ 'pizzas': pizzas })
