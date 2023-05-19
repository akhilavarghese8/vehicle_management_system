from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,FormView,View
from vehicle.forms import RegistrationForm,LoginForm,VehicleForm
from django.urls import reverse_lazy
from vehicle.models import Vehicle,User,AbstractUser
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

# Create your views here.

from django.contrib import messages

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('signin')
            
        else:
           return fn(request,*args,**kwargs)
    return wrapper


def superadmin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.role == 'superadmin':
            return fn(request,*args,**kwargs)
        else:
            return redirect('signin')
    return wrapper



def admin_or_superadmin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.role in ['superadmin','admin']:
            return fn(request,*args,**kwargs)
        else:
            return redirect('signin')       
    return wrapper
decs=[never_cache,admin_or_superadmin_required]
aces=[never_cache,superadmin_required]
cdes=[signin_required,never_cache]






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

@method_decorator(aces,name="dispatch")
class VehicleCreateView(CreateView):
    model=Vehicle
    template_name='vehicle_create.html'
    form_class=VehicleForm
    success_url=reverse_lazy("home")
    

    



@method_decorator(cdes,name="dispatch")
class IndexView(ListView):            
    model=Vehicle
    form_class=VehicleForm
    template_name='index.html'
    context_object_name="vehicle"
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
   

@method_decorator(decs,name="dispatch")
class VehicleUpdateView(UpdateView):
    model=Vehicle
    form_class=VehicleForm
    template_name="vehicle_update.html"
    pk_url_kwarg='id'
    success_url=reverse_lazy("home")    


@method_decorator(aces,name="dispatch")
class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vehicle.objects.filter(id=id).delete()     
        return redirect("home") 
        
    












