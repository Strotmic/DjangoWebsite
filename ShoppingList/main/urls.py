from django.urls import path
from . import views
from main.views import productList

urlpatterns = [
    path('hello/', views.say_hello),
    path('productlist/', productList.as_view()),
    
]