from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Admin_login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)