from ast import main
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('',views.register,name='register'),
    path('',views.login,name='login'),
   
   
]  