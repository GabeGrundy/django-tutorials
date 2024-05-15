from django.urls import path, include
from . import views 

urlpatterns = [
    path('base/', views.base,  name= 'base'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/',views.students, name='students'),
    path('studentform/',views.studentform, name='studentform'),
    path('teachers/',views.teachers, name='teachers'),
    path('', views.home,  name= 'home'),
    path('profile/', views.profile,  name= 'profile'),
    path('accounts/',include('django.contrib.auth.urls')),
]


