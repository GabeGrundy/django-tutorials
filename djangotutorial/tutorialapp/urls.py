from django.urls import path, include
from . import views 

urlpatterns = [
    path('base/', views.base,  name= 'base'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/',views.students, name='students'),
    path('teachers/',views.teachers, name='teachers'),
    path('', views.home,  name= 'home'),
    path('signup/', views.signup,  name= 'signup'),
    path('login/', views.login,  name= 'login'),
]


