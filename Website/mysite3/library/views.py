
from django.shortcuts import render
import email
from pipes import Template
from re import template
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, RedirectView
from django.contrib import messages

# from crud_project import enroll
from .forms import UserRegistration
from .models import User,Book,Book_Ranted




    

def index(request,form='sikandar'):
    user=User.objects.all()
    Total_User=0
    for i in range(len(user)):
        Total_User=Total_User+1
        
   

    Query_results = Book_Ranted.objects.all()
    Total_ranted_book=0
    for i in range(len(Query_results)):
        # Total_book=Total_book+i.num_books
        Total_ranted_book = Total_ranted_book + Query_results[i].num_ranted_books

    query_results = Book.objects.all()
    Total_book=0
    for i in range(len(query_results)):
        # Total_book=Total_book+i.num_books
        Total_book = Total_book + query_results[i].num_books
    Resrved_book=Total_book-Total_ranted_book
    context = { 'query_results' : query_results, 'total_book':Total_book,'total_user':Total_User,'total_ranted_book':Total_ranted_book,'resrved_book':Resrved_book,'f':form }

    return render(request,'home.html',context)
def book(request):
    query_results = Book.objects.all()
    # Total_book=0
    # Total_book = sum([item.num_books for item in query_results]) # Definitely takes more memory.
    context = { 'query_results' : query_results}
    

    # Returning the rendered html
    # return render(request, "review.html", context)
    return render(request,'book.html',context)

def user(request):
    stud=User.objects.all()

    return render(request,'User.html',context={'user': stud})


    
from . import forms
def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        f=form['username'].value
        if form.is_valid():
            # return render(request, 'Home.html', context={'form': form}) 
            return index(request,f)
            # return redirect('home')

        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    return render(request, 'login.html', context={'form': form})
 
def add_show(request):
    if request.method=='POST':
        fm=UserRegistration(request.POST)
        if fm.is_valid():
            print('Hloooooooooooooooooooo')
            nm=fm.cleaned_data['User_name']
            # reg=fm.cleaned_data['Reg_no']
            ema=fm.cleaned_data['Email']
            pas=fm.cleaned_data['Password']
            reg= User(User_name=nm,Email=ema,Password=pas)
            reg.save()
            fm=UserRegistration()
            # return render(request,'login.html')

            # return login_page(request)
            
    else:
        fm=UserRegistration()
    stud=User.objects.all()


    return render(request,'sign_up.html',{'form':fm,'stu':stud})   