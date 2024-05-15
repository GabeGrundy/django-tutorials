from ast import Lambda
from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import *
from .forms import *
from django.contrib import messages
# Create your views here.

def base(request):
    context={
    }
    
    return render(request, 'base.html', context)
@user_passes_test(lambda u: u.groups.filter(name='Teachers').exists())
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

@login_required 
def dashboard(request):
    context={
    }
    
    return render(request, 'dashboard.html', context)

def teachers(request):
    
    #query the database and save all students to a list
    teachers = Teacher.objects.all()
    
    #send all variables and objects and lists to the template
    context={
        'teachers': teachers,
    }
    return render(request, 'teachers.html', context)



def login(request):
    context={}
    
    return render(request, 'login.html', context)

@user_passes_test(lambda u: u.groups.filter(name='Teachers').exists())
def studentform(request):
    context={}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            context= ''
            for name, value in form.cleaned_data.items():
                print('{}: ({} {}'.format\
                    (name,type(value),value))
    
        requests = form.save(commit=False)

        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        middletname = form.cleaned_data['middlename']
        grade  = form.cleaned_data['grade']
        requests.save()

        messages.success(request, "New Student Added Successfully!")

    else:
        form = StudentForm()

    
    return render(request,'studentform.html',\
        {'method':request.method,"form":form}
        )

@user_passes_test(lambda u: u.groups.filter(name='Admins').exists())
def studentform(request):
    context={}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            context= ''
            for name, value in form.cleaned_data.items():
                print('{}: ({} {}'.format\
                    (name,type(value),value))
    
        requests = form.save(commit=False)

        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        middletname = form.cleaned_data['middlename']
        grade  = form.cleaned_data['grade']
        requests.save()

        messages.success(request, "New Student Added Successfully!")

    else:
        form = StudentForm()

    
    return render(request,'studentform.html',\
        {'method':request.method,"form":form}
        )






    return render(request, 'studentform.html', context)    


def profile(request):
    context={}
    
    return render(request, 'profile.html', context)