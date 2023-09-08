from django import forms

class StudentForms(forms.Form):
    Sname  = forms.CharField()
    Sid = forms.IntegerField()
    Semail = forms.EmailField()