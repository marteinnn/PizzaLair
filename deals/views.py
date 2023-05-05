from django.shortcuts import render
from deals.models import Deals
# Create your views here.
def deals(request):
    return render(request, 'deals/index.html', {
        'alldeals': Deals.objects.all()
    })
