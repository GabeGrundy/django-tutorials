from multiprocessing import context
from django.shortcuts import render
from .models import *


# Create your views here.
def base(request):
    context={
    }
    
    return render(request, 'base.html', context)

def students(request):
    
    #query the database and save all students to a list
    students = Student.objects.all()
    
    #send all variables and objects and lists to the template
    context={
        'students': students,
    }
    
    
    return render(request, 'students.html', context)

def home(request):
    context={
    }
    
    return render(request, 'base.html', context)


def dashboard(request):
    context={
    }
    
    return render(request, 'dashboard.html', context)

def teachers(request):
    context={
    }
    
    return render(request, 'teachers.html', context)