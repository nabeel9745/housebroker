from contextlib import redirect_stdout
# from curses import use_default_colors
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
        if 'reject' in request.POST:
                store_to.approved='rejected'      
        if 'accept' in request.POST:
                store_to.approved=('approved')
                store_to.save()
   return render(request,'houseadmin/accept.html',{'viewreq':request_data})

def v_owners(request):
           artist_info=User_registration.objects.filter(approved='approved')
           return render(request,'houseadmin/view_owners.html',{'view_owners':artist_info})  

def delete_owners(req,id):
    User_registration.objects.get(id=id).delete()
    return redirect('v_owners')

        
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
         







