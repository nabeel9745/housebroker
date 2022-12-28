# from re import M
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

# Create your models here.

class listed_property(models.Model):
    prop_name = models.CharField(max_length=100)
    prop_address = models.CharField(max_length=100)
    prop_landmark = models.CharField(max_length=100)
    prop_pincode = models.BigIntegerField()

class User_registration(models.Model):
    owner_name = models.CharField(max_length=50)
    owner_phn = models.BigIntegerField()
    owner_email =models.CharField(max_length=50)
    owner_password =models.CharField(max_length=50)
    approved = models.CharField(max_length=80,default='not approved')
