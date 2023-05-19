from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,FormView,TemplateView,DetailView,View
from vehicle.forms import RegistrationForm,LoginForm,VehicleForm
from django.urls import reverse_lazy
from vehicle.models import Vehicle,User,AbstractUser
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages



def superadminsignin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.role=='superadmin':
            return fn(request,*args,**kwargs)
        else:
            return redirect('error')
    return wrapper

superadmindecs=[superadminsignin_required,never_cache]

def adminsignin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.role=='admin':
            return fn(request,*args,**kwargs)
        else:
            return redirect('error')       
    return wrapper

admindecs=[adminsignin_required,never_cache]

def usersignin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.role=='user':
            return fn(request,*args,**kwargs)
        else:
            return redirect('error')       
    return wrapper

userdecs=[usersignin_required,never_cache]






class SignUpView(CreateView):

    model=User
    form_class=RegistrationForm
    template_name="registration.html"
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        return super().form_valid(form)
    



class SignInView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            usrn=form.cleaned_data.get("username")
            passw=form.cleaned_data.get("password")
            usr=authenticate(request,username=usrn,password=passw)
            if usr:
                login(request,usr)
                return redirect('home')
                       
            else:
                messages.error(request, 'Invalid username and passwod, Please try again.')
                return render(request,"login.html",{"form":form})
            

       

def SignOutView(request,*args,**kwargs):
    logout(request)
    return redirect('signin')

@method_decorator(superadmindecs,name="dispatch")
class VehicleCreateView(CreateView):
    model=Vehicle
    template_name='vehicle_create.html'
    form_class=VehicleForm
    success_url=reverse_lazy("home")
    k_url_kwarg='id'



# @method_decorator(superadmindecs,userdecs,admindecs,name="dispatch")
class IndexView(ListView):            
    model=Vehicle
    form_class=VehicleForm
    template_name='index.html'
    context_object_name="vehicle"
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
   

@method_decorator(superadmindecs,name="dispatch")
class VehicleUpdateView(UpdateView):
    model=Vehicle
    form_class=VehicleForm
    template_name="vehicle_update.html"
    pk_url_kwarg='id'
    success_url=reverse_lazy("home")    


@method_decorator(superadmindecs,name="dispatch")
class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vehicle.objects.filter(id=id).delete()     
        return redirect("home")    
    












