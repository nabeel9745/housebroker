from urllib import request
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import*
from django.http import JsonResponse



# Create your views here.

def home(request):
    return render(request,'owners/home.html')

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
    


    
