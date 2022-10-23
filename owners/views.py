from contextlib import redirect_stderr
from urllib import request
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from .models import*
from django.http import JsonResponse



# Create your views here.

def home(request):
    return render(request,'owners/home.html')

def navbar(request):
    return render(request,'owners/navbar.html')

def login(request):
    error1=''
    error2=''
    if request.method =='POST':
        o_eml =request.POST['l_email']
        o_psd =request.POST['l_psd']
        try:
            owner_log = User_registration.objects.get(owner_email=o_eml,owner_password=o_psd)
            approve = owner_log.approved
            if approve == 'approved':
                request.session['owner_id']=owner_log.id
                return redirect('welcome')
            else:
                error1="admin should approve"
                return render(request,'owners/login.html',{'err':error1})
        except:
            error2="invalid email id or password"
    return render(request,'owners/login.html',{'errr':error2})

 
def account(request):
    return render(request,'owners/account.html')

def listed_prop(request):
    return render(request,'owners/listed_prop.html')

def property_up(request):
    return render(request,'owners/property_update.html')

def addapart(request):
    return render(request,'owners/addapart.html')
@csrf_exempt
def list_url(req):
    n = req.POST['n_data']
    a = req.POST['a_data']
    l = req.POST['l_data']
    p = req.POST['p_data']
    listed_property(prop_name=n,prop_address=a,prop_landmark=l,prop_pincode=p).save()
    return JsonResponse({'message':'value'})
    
def list_prop(request):
     valu = listed_property.objects.all()
     full_value = [{'v':i.id,'v1':i.prop_name,'v2':i.prop_address,'v3':i.prop_landmark,'v4':i.prop_pincode}for i in valu]
     return JsonResponse({'display':full_value})

def registration (request):
    text_msg=''
    if request.method == 'POST':
        re_name = request.POST['r_name']
        re_phn = request.POST['r_phn']
        re_eml = request.POST['r_email']
        re_psd = request.POST['r_psd']
        User_registration(owner_name=re_name,owner_phn=re_phn,owner_email=re_eml,owner_password=re_psd).save()
        text_msg='admin should approve your request'
    return render(request,'owners/registration.html',{'msg':text_msg})

def welcome (request):
    current_owner = request.session['owner_id']
    naming = User_registration.objects.get(id=current_owner)
    return render(request,'owners/welcome_window.html',{'profil':naming})


    


    
