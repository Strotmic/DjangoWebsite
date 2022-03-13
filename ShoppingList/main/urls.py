from django.urls import path
from . import views
from main.views import productList

urlpatterns = [
    path('hello/', views.tabel),
    path('add/', views.add_product),
    path('delete/', views.delete_product),
    path('productlist/', productList.as_view()),
    
]