from django.shortcuts import render

# Create your views here.

def home(request):
        return render(request,'houseadmin/index.html')

def face(request):
     return render(request,'houseadmin/face.html')     

def house(request):
     return render(request,'houseadmin/house.html')   

def controls(request):
     return render(request,'houseadmin/controls.html')       

def adminhome(request):
     return render(request,'houseadmin/adminhome.html')       

