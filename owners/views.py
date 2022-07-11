from django.shortcuts import render

# Create your views here.

def hello (request):
    return render(request,'owners/hello.html')

def contactadmin (request):
    return render(request,'owners/connectadmin.html') 

def home(request):
    return render(request,'owners/home.html')