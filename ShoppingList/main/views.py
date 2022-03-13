from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.pyplot import connect
import mysql.connector
from mysql.connector import Error
import re

from numpy import size

mysql.connector.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='shoppinglist')
con = connection.cursor()
products= {}
  
def calculate_aantal():
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
        products= {'naam':naam,'aantal':int(aantal),'gewichteen':float(gewichteen),'gewichttotaal':float(gewichttotaal)}
    return products

def isnodig():
    x = calculate_aantal()
    if(x<=1):
        con.execute("update products")

def fruitsap():
    return True
def say_hello(request):
    x = calculate_aantal()
    z = x
    naam = x['naam']
    aantal = x['aantal']
    gewichteen = x['gewichteen']
    gewichttotaal = x['gewichttotaal']
    return render(request, 'test.html', {'naam':naam, 'aantal':aantal,'gewichteen':gewichteen, 'gewichttotaal':gewichttotaal})

    

# Create your views here.
