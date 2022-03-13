from django.shortcuts import render
from matplotlib.style import context
from main.models import *
from django.shortcuts import redirect

def tabel(request):
    isnodig()
    x = calculate_aantal()
    z = x
    for obj in x:
        naam = obj.name
        aantal = obj.aantal
        gewichteen = obj.weight
        gewichttotaal = obj.total_weight
        kopen = obj.order
    return render(request, 'test.html', {'lijst':x})

def add_product(request):
    z = con.execute("select * from products")
    if request.method == 'POST':
        name = request.POST['name']
        aantal = request.POST['aantal']
        weight = request.POST['weight']
        total_weight = float(weight)*float(aantal)
        done =False
        new_product = winkelProduct(z+1,name,weight,aantal,total_weight,done)
        con.execute(f"insert into products(id,naam,aantal,gewicht_een,gewicht_totaal,nodig) values({z+1},'{name}',{aantal},{weight},{total_weight},{done})")
        tabel(request)
        return redirect('/main/hello/')
        pass
    return render(request, 'addProduct.html')

def delete_product(request):
    con.execute(f"DELETE FROM products WHERE id={request.POST['id']}")
    return redirect('/main/hello/')
# Create your views here.
