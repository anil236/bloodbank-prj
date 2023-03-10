from audioop import add
from contextlib import redirect_stderr
import email
from http.client import HTTPResponse
from django.shortcuts import render , redirect
from django.http import HttpResponse


# Create your views here.

def home(request):
    return  render(request,'index.html')

def contact(request):
    return  render(request,'contactus.html')

def register(request):
    return  render(request,'register.html')

def login(request):
    return render(request,'login.html')
   
    #------------ donate , request , stock-----------
 