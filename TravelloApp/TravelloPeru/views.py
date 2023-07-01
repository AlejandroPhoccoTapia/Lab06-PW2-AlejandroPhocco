from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    destinations = Destination.objects.all()

    return render(request, 'index.html', {'destinations': destinations})

def destination(request, id):
    destination = Destination.objects.get(id=id)
    return render(request, 'destination.html', {'destination': destination})