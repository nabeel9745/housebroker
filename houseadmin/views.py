from contextlib import redirect_stdout
from django.shortcuts import render,redirect
from houseadmin.models import Admin_login
from owners.models import User_registration


# Create your views here.

def adminhome(request):
        return render(request,'houseadmin/adminhome.html') 

def master_a(request):
        return render(request,'houseadmin/admin_master.html')   

def accept(request):
   request_data = User_registration.objects.filter(approved='not approved')
   if request.method == 'POST':
        store_to = User_registration.objects.get(id=request.POST['id'])
        if 'approve' in request.POST:
                store_to.approved='approved'
        if 'reject' in request.POST:
                store_to.approved='rejected'
                store_to.save()
   return render(request,'houseadmin/accept.html',{'viewreq':request_data})

def v_owners(request):
        return render(request,'houseadmin/view_owners.html')   

def r_prop(request):
        return render(request,'houseadmin/reg_properties.html')  
 
def a_login(request):
            error=''
            if request.method == 'POST':
                admin_u = request.POST['admin_user']
                admin_p = request.POST['admin_pass']
                try:
                        admin_data=Admin_login.objects.get(username=admin_u,password=admin_p)
                        request.session['admin_id']=admin_data.id
                        return redirect ('adminhome')
                except:
                        error='invaid'
            return render(request,'houseadmin/admin_login.html',{'error':error})  
         







