from django.urls import path
from .import views

# app_name='houseadmin'

urlpatterns=[
   path('index',views.index),
   path('adminhome',views.adminhome),
   path('master_a',views.master_a),


]
