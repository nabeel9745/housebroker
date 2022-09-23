from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'owners/home.html')

def addapart(request):
    return render(request,'owners/addapart.html')

def navbar(request):
    return render(request,'owners/navbar.html')

def login(request):
    return render(request,'owners/login.html')

def account(request):
    return render(request,'owners/account.html')

def listed_prop(request):
    return render(request,'owners/listed_prop.html')

def property_up(request):
    return render(request,'owners/property_update.html')


