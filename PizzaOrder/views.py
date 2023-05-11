from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from menu.models import Pizza, PizzaToppings

# Create your views here.
def order(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = []
        for pizza in Pizza.objects.filter(name__icontains=search_filter):
            pizza_dict = {'id': pizza.PID, 'name': pizza.name, 'price': pizza.price, 'image': pizza.image,
                          'description': pizza.description, 'spicy': pizza.spicy, 'vegan': pizza.vegan,
                          'toppings': [" " + topping.name for topping in pizza.pizzatoppings_set.all()]}
            pizzas.append(pizza_dict)
        return JsonResponse({'data': pizzas})
    elif 'check_filter' in request.GET:
        filter = request.GET['check_filter']
        if filter == 'vegan':
            pizzas = []
            for pizza in Pizza.objects.filter(vegan__icontains=True):
                pizza_dict = {'id': pizza.PID, 'name': pizza.name, 'price': pizza.price, 'image': pizza.image,
                              'description': pizza.description, 'spicy': pizza.spicy, 'vegan': pizza.vegan,
                              'toppings': [" " + topping.name for topping in pizza.pizzatoppings_set.all()]}
                pizzas.append(pizza_dict)
            return JsonResponse({'data': pizzas})
        elif filter == 'spicy':
            pizzas = []
            for pizza in Pizza.objects.filter(spicy__icontains=True):
                pizza_dict = {'id': pizza.PID, 'name': pizza.name, 'price': pizza.price, 'image': pizza.image,
                              'description': pizza.description, 'spicy': pizza.spicy, 'vegan': pizza.vegan,
                              'toppings': [" " + topping.name for topping in pizza.pizzatoppings_set.all()]}
                pizzas.append(pizza_dict)
            return JsonResponse({'data': pizzas})
        elif filter == 'sortbyname':
            pizzas = []
            for pizza in Pizza.objects.all().order_by('name'):
                pizza_dict = {'id': pizza.PID, 'name': pizza.name, 'price': pizza.price, 'image': pizza.image,
                              'description': pizza.description, 'spicy': pizza.spicy, 'vegan': pizza.vegan,
                              'toppings': [" " + topping.name for topping in pizza.pizzatoppings_set.all()]}
                pizzas.append(pizza_dict)
            return JsonResponse({'data': pizzas})

        elif filter == 'sortbyprice':
            pizzas = []
            for pizza in Pizza.objects.all().order_by('price'):
                pizza_dict = {'id': pizza.PID, 'name': pizza.name, 'price': pizza.price, 'image': pizza.image,
                              'description': pizza.description, 'spicy': pizza.spicy, 'vegan': pizza.vegan,
                              'toppings': [" " + topping.name for topping in pizza.pizzatoppings_set.all()]}
                pizzas.append(pizza_dict)
            return JsonResponse({'data': pizzas})

    pizzas = []
    for pizza in Pizza.objects.all():
        toppings = pizza.pizzatoppings_set.all()
        pizzas.append({'pizza': pizza, 'toppings': toppings})
    context = {'pizzas': pizzas}
    return render(request, 'order/index.html', context)


def get_pizza_by_id(request, id):
    return render(request, 'order/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, PID=id)
    })