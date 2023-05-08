from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from menu.models import Pizza, PizzaToppings, Topping

# Create your views here.
def order(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = [ {
            'id': x.PID,
            'name': x.name,
            'price': x.price,
            'image': x.image,
            'description': x.description,
            'spicy': x.spicy,
            'vegan': x.vegan
        } for x in Pizza.objects.filter(name__icontains=search_filter)]
        return JsonResponse({ 'data': pizzas })
    elif 'check_filter' in request.GET:
        filter = request.GET['check_filter']
        if filter == 'vegan':
            pizzas = [{
                'id': x.PID,
                'name': x.name,
                'price': x.price,
                'image': x.image,
                'description': x.description,
                'spicy': x.spicy,
                'vegan': x.vegan
            } for x in Pizza.objects.filter(vegan__icontains=True)]
            return JsonResponse({'data': pizzas})
        elif filter == 'spicy':
            pizzas = [{
                'id': x.PID,
                'name': x.name,
                'price': x.price,
                'image': x.image,
                'description': x.description,
                'spicy': x.spicy,
                'vegan': x.vegan
            } for x in Pizza.objects.filter(spicy__icontains=True)]
            return JsonResponse({'data': pizzas})
        elif filter == 'sortbyname':
            pizzas = [{
                'id': x.PID,
                'name': x.name,
                'price': x.price,
                'image': x.image,
                'description': x.description,
                'spicy': x.spicy,
                'vegan': x.vegan
            } for x in Pizza.objects.all().order_by('name')]
            return JsonResponse({'data': pizzas})

        elif filter == 'sortbyprice':
            pizzas = [{
                'id': x.PID,
                'name': x.name,
                'price': x.price,
                'image': x.image,
                'description': x.description,
                'spicy': x.spicy,
                'vegan': x.vegan
            } for x in Pizza.objects.all().order_by('price')]
            return JsonResponse({'data': pizzas})

    return render(request, 'order/index.html', {
        'pizzas': Pizza.objects.all()
    })

def get_pizza_by_id(request, id):
    return render(request, 'order/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, PID=id)
    })

