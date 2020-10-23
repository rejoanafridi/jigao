from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.


def login(request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            if request.method == 'GET':
                return render(request, 'account/login.html')

            elif request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('login')
                else:
                    return render(request, 'account/login.html', {'msg': 'Invalid username and password'})

def logout(request):
    auth_logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'GET':
            return render(request,'account/register.html')
        elif request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            username_count = User.objects.filter(username=username).count()
            email_count = User.objects.filter(email=email).count()

            if username_count == 0 and email_count == 0:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('login')

            elif username_count > 0:
                return render(request, 'account/register.html', {'msg': 'This username is in used'})

            elif email_count > 0:
                return render(request, 'account/register.html', {'msg': 'This email is in used'})





    