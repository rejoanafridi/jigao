from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import forms

# Create your views here.


def index(request):
        if request.user.is_authenticated:
            return render(request, 'main/index.html')
        else:
            return render(request, 'account/login.html')

def login(request):
        if request.user.is_authenticated:
            return render(request, 'main/index.html')
        else:
            if request.method == 'GET':
                return render(request, 'account/login.html')

            elif request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('/')
                else:
                    return render(request, 'account/login.html', {'msg': 'Invalid username and password'})

def logout(request):
    auth_logout(request)
    return redirect('login')

def register(request):
    return render(request,'account/register.html')