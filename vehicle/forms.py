from django import forms
from django.contrib.auth.models import AbstractUser
from vehicle.models import User,Vehicle
from django.contrib.auth.forms import UserCreationForm


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']

    widgets={
            'vehicle_number':forms.TextInput(attrs={'placeholder':'Enter your vehiclenumber','class':'form-control'}),
            'vehicle_type':forms.TextInput(attrs={'placeholder':'Enter your vehicletype','class':'form-control'}),
            'vehicle_model':forms.EmailInput(attrs={'placeholder':'Enter your vehiclemodel','class':'form-control'}),
            'vehicle_description':forms.TextInput(attrs={'placeholder':'Enter your vehicledescription','class':'form-control'}),
    }



class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2","role"]
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'Enter your firstname','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter your lastname','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email','class':'form-control'}),
            'username':forms.TextInput(attrs={'placeholder':'Enter your firstname','class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'placeholder':'Enter your firstname','class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'placeholder':'Enter your firstname','class':'form-control'}),
            'role':forms.RadioSelect(attrs={'placeholder':'Enter your firstname','class':'form-control'}),


        }


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
