from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    contactnumber = models.FloatField()
    description = models.CharField(max_length = 100)
