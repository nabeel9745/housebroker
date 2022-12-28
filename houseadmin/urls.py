from django.urls import path
from .import views

# app_name='houseadmin'

urlpatterns=[
   path('adminhome',views.adminhome,name='adminhome'),
   path('master_a',views.master_a,name='master_a'),
   path('accept',views.accept,name='accept'),
   path('v_owners',views.v_owners,name='v_owners'),
   path('delete_owners/<int:id>',views.delete_owners,name='delete_owners'),
   path('r_prop',views.r_prop,name='r_prop'),
   path('a_login',views.a_login,name='a_login'),
   
   
]
