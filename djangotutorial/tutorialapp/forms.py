from dataclasses import fields
from importlib.metadata import files
from socket import fromshare
from django import fromshare
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname','lastname','middlename','grade']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname','lastname','middlename','class']