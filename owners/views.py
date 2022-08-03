from django.shortcuts import render

# Create your views here.

def hello (request):
    return render(request,'owners/hello.html')

def contactadmin (request):
    return render(request,'owners/connectadmin.html') 

def home(request):
    return render(request,'owners/home.html')

def addapart(request):
    return render(request,'owners/addapart.html')

def navbar(request):
    return render(request,'owners/navbar.html')

