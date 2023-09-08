from django.shortcuts import render
from app.forms import *
from app.models import *

def Insert_student(request):
    SFO = StudentForms()
    d = {'SFO' : SFO } 
    if request.method=='POST':
        SFDO = StudentForms(request.POST)
        if SFDO.is_valid():

            Sname = SFDO.cleaned_data['Sname']
            Sid = SFDO.cleaned_data['Sid']
            Semail = SFDO.cleaned_data['Semail']

            SO = Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            SO.save()
    return render(request,'Insert_student.html',d)