from django.urls import path
from .import views
urlpatterns = [
path('',views.Home,name='Home'),
path('about/',views.About,name='about'),
path('services/',views.Services,name='Services'),
path('contactus/',views.Contactus,name='Contactus'),
]