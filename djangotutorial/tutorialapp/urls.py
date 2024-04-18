from django.urls import path, include
from . import views 

urlpatterns = [
    path('base/', views.base,  name= 'base'),    
    #path('dashboard/', views.dashboard, name='dashboard')
    #path('', views.home,  name= 'home'),

]


