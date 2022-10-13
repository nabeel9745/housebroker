from django.urls import path
from .import views

# app_name='owners'

urlpatterns=[
   path('home',views.home,name='home'),
   path('navbar',views.navbar),
   path('login',views.login),
   path('account',views.account,name='account'),
   path('property_up',views.property_up,name='property_up'),
   path('addapart',views.addapart,name='addapart'),
   path('listed_prop',views.listed_prop,name='listed_prop'),
   path('list_url',views.list_url,name='list_url'),
   path('list_prop',views.list_prop,name='list_prop'),

   






]