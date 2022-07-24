from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django.core import validators
from django import forms
from .models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['User_name','Email','Password']
        widgets={
            'User_name':forms.TextInput(attrs={'autofocus': 'autofocus',
                                      'autocomplete': 'off',
                                      'size': '40',
                                      'font-size': 'xx-large',
                                      'style': 'border-color:darkgoldenrod; border-radius: 10px;'
                                      }),
            # 'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'autofocus': 'autofocus',
                                      'autocomplete': 'off',
                                      'size': '40',
                                      'font-size': 'xx-large',}),
            'Password':forms.PasswordInput(attrs={'autofocus': 'autofocus',
                                      'autocomplete': 'off',
                                      'size': '40',
                                      'font-size': 'xx-large',}),

            # 'Semester':forms.NumberInput(attrs={'class':'form-control'}),


            # 'Password':forms.PasswordInput(attrs={'class':'form-control'

            
        }
        fields = '__all__'

from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

