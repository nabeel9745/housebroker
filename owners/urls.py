from django.urls import path
from .import views

# app_name='owners'

urlpatterns=[
   path('homes',views.homes,name='homes'),
   path('navbar',views.navbar),
   path('owners_login',views.owners_login,name='owners_login'),
   path('account',views.account,name='account'),
   path('edit_account/<int:id>',views.edit_account,name='edit_account'),
   path('property_up',views.property_up,name='property_up'),
   path('addapart',views.addapart,name='addapart'),
   path('listed_prop',views.listed_prop,name='listed_prop'),
   path('list_url',views.list_url,name='list_url'),
   path('list_prop',views.list_prop,name='list_prop'),
   path('registration',views.registration,name='registration'),
   path('welcome',views.welcome,name='welcome'),



   






]