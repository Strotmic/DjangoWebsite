from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x=1
    y=2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'test.html', {'name':'Tim'})

    

# Create your views here.
