from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    role = [
        ('superadmin', 'superadmin'),
        ('admin', 'admin'),
        ('user', 'user'),
    ]

    
    role = models.CharField(max_length=200, choices=role)
    def __str__(self) :
          return self.first_name

class Vehicle(models.Model):
    vehicle_type = [
        ('Two Wheeler', 'Two Wheeler'),
        ('Three Wheeler', 'Three Wheeler'),
        ('Four Wheeler', 'Four Wheeler'),
    ]

    vehicle_number = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100, choices=vehicle_type)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.CharField(max_length=100)

    def __str__(self) :
         return self.vehicle_model
         

