from django.shortcuts import redirect, render
from django.contrib.auth import get_user


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        user = get_user(request)
        return render(request, "main/index.html",{'usr':user})
    else:
        return redirect('account/login')


def test(request):
    return render(request, 'base.html')


