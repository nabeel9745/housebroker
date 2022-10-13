from re import M
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class listed_property(models.Model):
    prop_name = models.CharField(max_length=100)
    prop_address = models.CharField(max_length=100)
    prop_landmark = models.CharField(max_length=100)
    prop_pincode = models.BigIntegerField()