from django.shortcuts import render
# Create your views here.
def deals(request):
    return render(request, 'deals/index.html')