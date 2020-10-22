from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, "main/index.html")
    else:
        return redirect('account/login')


def test(request):
    return render(request, 'base.html')


