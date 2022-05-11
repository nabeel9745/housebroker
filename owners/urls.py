from django.urls import path
from .import views

app_name='owners'

urlpatterns=[
   path('hello',views.hello,name='hello'),
   path('contactadmin',views.contactadmin),
]