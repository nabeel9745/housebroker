from django.shortcuts import render

# Create your views here.

def loginexample(request):
    return render(request,'users/loginexample.html')

def home(request):
    return render(request,'users/home.html')

def login (request):
     return render(request,'users/loginpage.html') 

def registration (request):
    return render(request,'users/registration.html')
 
def apartments (request):
    return render(request,'users/apartments.html')

def boot (request):
    return render(request,'users/bootregistration.html')

def details (request):
    return render(request,'users/details.html')