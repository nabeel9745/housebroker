from django.shortcuts import render

# Create your views here.

def index(request):
        return render(request,'houseadmin/index.html')    

def adminhome(request):
        return render(request,'houseadmin/adminhome.html') 

def master_a(request):
        return render(request,'houseadmin/admin_master.html')   

def accept(request):
        return render(request,'houseadmin/accept.html')    

def v_owners(request):
        return render(request,'houseadmin/view_owners.html')   

def r_prop(request):
        return render(request,'houseadmin/reg_properties.html')  

