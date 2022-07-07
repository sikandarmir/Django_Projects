from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django.core import validators
from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','Reg_no','email','Semester']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'Reg_no':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'Semester':forms.NumberInput(attrs={'class':'form-control'}),


            # 'Password':forms.PasswordInput(attrs={'class':'form-control'

            
        }
        # fields = '__all__'

