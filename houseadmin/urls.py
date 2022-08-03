from django.urls import path
from .import views

app_name='houseadmin'

urlpatterns=[
   path('index',views.home),
   path('face',views.face,name='faces'),
   path('house',views.house,),
   path('controls',views.controls),
   path('adminhome',views.adminhome),

]
