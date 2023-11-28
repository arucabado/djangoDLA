from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('adduser/', views.adduser, name='adduser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('actuser/', views.actuser, name='actuser'),
    path('horarios/', views.horarios, name='Horarios'),
]