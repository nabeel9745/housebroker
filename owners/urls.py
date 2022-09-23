from django.urls import path
from .import views

# app_name='owners'

urlpatterns=[
   path('home',views.home,name='home'),
   path('addapart',views.addapart,name='addapart'),
   path('navbar',views.navbar),
   path('login',views.login),
   path('account',views.account,name='account'),
   path('listed_prop',views.listed_prop,name='listed_prop'),
   path('property_up',views.property_up,name='property_up'),






]