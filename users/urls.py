from django.urls import path
from .import views

# app_name='users'

urlpatterns=[
   path('logincreation',views.logincreation,name='login'),
   path('home',views.home),
   path('login',views.login,name='login'),
   path('apartments',views.apartments,name='apartments'),
   path('boot',views.boot),
   path('details',views.details),
   path('master',views.master),
   path('hotel',views.hotel,name='hotel'),
   path('otp',views.otp),
   path('book',views.book,name='book'),
   path('confirmation',views.confirmation,name='confirmation'),




]