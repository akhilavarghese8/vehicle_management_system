from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.

class User(AbstractUser):
    role = [
        ('superadmin', 'superadmin'),
        ('admin', 'admin'),
        ('user', 'user'),
    ]

    
    role = models.CharField(max_length=200, choices=role,default='user')
    def __str__(self) :
          return self.first_name

class Vehicle(models.Model):
    vehicle_type = [
        ('Two Wheeler', 'Two Wheeler'),
        ('Three Wheeler', 'Three Wheeler'),
        ('Four Wheeler', 'Four Wheeler'),
    ]
    alphanumeric=RegexValidator(r"^[0-9a-zA-Z_]*$",'Only use alphanumeric characters')
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    vehicle_number = models.CharField(max_length=100,validators=[alphanumeric])
    vehicle_type = models.CharField(max_length=100, choices=vehicle_type,default='Two Wheeler',null=True)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.CharField(max_length=100)

    def __str__(self) :
         return self.vehicle_model
         

