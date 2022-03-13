from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    return 1

def say_hello(request):
    x = calculate()
    return render(request, 'test.html', {'name':'Tim'})

    

# Create your views here.
