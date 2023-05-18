from django.urls import path

from vehicle import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home/",views.IndexView.as_view(),name="home"),
    path('home/vehicles/<int:id>/delete/',views.VehicleDeleteView.as_view,name='vehicle-delete'),
    path('home/vehicles/create/',views.VehicleCreateView.as_view(), name='vehicle-create'),
    path('home/vehicles/<int:id>/update/',views.VehicleUpdateView.as_view(), name='vehicle-update'),
    
    path("logout/",views.SignOutView,name="signout"),
    
    

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
