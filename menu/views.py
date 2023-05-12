from django.shortcuts import render
from menu.models import Pizza

# Create your views here.
def menu(request):
    return render(request, 'menu/index.html', {
        'pizzas': Pizza.objects.all()
    })

def handler_404(request, exception):
    return render(request, '404.html')
