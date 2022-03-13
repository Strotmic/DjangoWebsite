from math import prod
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.pyplot import connect
import mysql.connector
from mysql.connector import Error
import re
from numpy import size
import socket
from main.models import winkelProduct
from django.views.generic import ListView



mysql.connector.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='shoppinglist')
con = connection.cursor()
products= []
class productList(ListView):
    model = winkelProduct

def calculate_aantal():
    products =[]
    longlist=[]
    z=con.execute("select * from products")
    for i in range(int(z)):
        i+=1
        longlist.append(i)
    for id in longlist:
        con.execute(f"select * from products where id = {id}")
        con.execute(f"select naam from products where id={id}")
        naam = con.fetchall()
        naam = re.sub("[(),]","",str(naam))
        con.execute(f"select gewicht_een from products where id={id}")
        gewichteen = con.fetchall()
        gewichteen = re.sub("[(),]","",str(gewichteen))
        z = con.execute(f"select gewicht_totaal from products where id={id}")
        gewichttotaal = con.fetchall()
        gewichttotaal = re.sub("[(),]","",str(gewichttotaal))
        if(type(gewichteen)==float):
            aantal = gewichttotaal/gewichteen
        else:
            aantal = float(gewichttotaal)/float(gewichteen)
        if aantal<2:
            order = True
        else:
            order = False
        products.append( winkelProduct(id,naam,gewichteen,gewichttotaal,aantal,order))
    return products

def isnodig():
    x = calculate_aantal()
    for obj in x:

        if(obj.aantal<=1):
            con.execute(f"update products set nodig=true where id={obj.id}")


def say_hello(request):
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

    

# Create your views here.
