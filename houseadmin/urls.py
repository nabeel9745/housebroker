from django.urls import path
from .import views

# app_name='houseadmin'

urlpatterns=[
   path('index',views.index),
   path('adminhome',views.adminhome),
   path('master_a',views.master_a),
   path('accept',views.accept,name='accept'),
   path('v_owners',views.v_owners,name='v_owners'),
   path('r_prop',views.r_prop,name='r_prop'),





]
