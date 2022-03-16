from django.db import models
from django.db import connection
from matplotlib.pyplot import cla
import mysql.connector
import re
from django.views.generic import ListView
from django.forms import ModelForm

class winkelProduct(models.Model):
    def __init__(self,id,name,weight,total_weight,aantal,order):
        self.id = id
        self.name = name
        self.weight = weight
        self.total_weight = total_weight
        self.aantal=aantal
        self.order = order
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getweight(self):
        return self.weight
    def gettotal_weight(self):
        return self.total_weight
    def getaantal(self):
        return self.aantal
    def getorder(self):
        return self.order
    def getAll(self):
        return f"{self.getname()} met gewicht {self.getweight()}kg en totaal gewicht {self.gettotal_weight()}kg. Aantal {self.getaantal()} moeten we kopen {self.getorder()}"
    def __str__(self):
        return f"{self.getname()} met gewicht {self.getweight()}kg en totaal gewicht {self.gettotal_weight()}kg. Aantal {self.getaantal()} moeten we kopen {self.getorder()}"

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
    ids=con.execute("select id from products")
    y=[]
    for row in con.fetchall():
        y+=row
    for id in y:

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
        else:
            con.execute(f"update products set nodig=false where id={obj.id}")


