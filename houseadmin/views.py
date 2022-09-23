from django.shortcuts import render

# Create your views here.

def index(request):
        return render(request,'houseadmin/index.html')    

def adminhome(request):
        return render(request,'houseadmin/adminhome.html') 

def master_a(request):
        return render(request,'houseadmin/admin_master.html')      


