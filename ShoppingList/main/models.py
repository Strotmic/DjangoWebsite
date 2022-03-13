from django.db import models

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
