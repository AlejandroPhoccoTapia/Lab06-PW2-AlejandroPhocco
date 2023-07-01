from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    destinations = Destination.objects.all()

    return render(request, 'index.html', {'destinations': destinations})

def destination(request, id):
    destination = Destination.objects.get(id=id)
    return render(request, 'destination.html', {'destination': destination})

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()

        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')