# from crypt import methods
import email
from django.shortcuts import render,HttpResponseRedirect

# from crud_project import enroll
from .forms import StudentRegistration
from .models import Student

# Create your views here.
#This Function will add new iteam and show all iteam 
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            reg=fm.cleaned_data['Reg_no']
            ema=fm.cleaned_data['email']
            seme=fm.cleaned_data['Semester']
            reg= Student(name=nm,Reg_no=reg,email=ema,Semester=seme)
            reg.save()
            fm=StudentRegistration()

    else:
        fm=StudentRegistration()
    stud=Student.objects.all()

    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#This function will Edit and update 

def update_data(request,id):
    if request.method =='POST':
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if  fm.is_valid():
            fm.save()
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request,'enroll/updatestudent.html',{'form':fm})




#This Function will Delate 
def delete_data(request, id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

