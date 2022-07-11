from django.urls import path
from .import views

app_name='users'

urlpatterns=[
   path('loginexample',views.loginexample,name='login'),
   path('home',views.home),
   path('login',views.login,name='login'),
   path('registration',views.registration),
   path('apartments',views.apartments),
   path('boot',views.boot),
   path('details',views.details),


   


]