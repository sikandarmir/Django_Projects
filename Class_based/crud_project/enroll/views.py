# from crypt import methods
import email
from pipes import Template
from re import template
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, RedirectView

# from crud_project import enroll
from .forms import StudentRegistration
from .models import Student


# # Create your views here.
# #This Class will add new iteam and show all iteam 
class UserAddshowView(TemplateView):
    template_name='enroll/addandshow.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        fm=StudentRegistration()
        stud=Student.objects.all()
        context={'stu':stud,'form':fm}
        return context
    def post (self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            reg=fm.cleaned_data['Reg_no']
            ema=fm.cleaned_data['email']
            seme=fm.cleaned_data['Semester']
            reg= Student(name=nm,Reg_no=reg,email=ema,Semester=seme)
            reg.save()
            return HttpResponseRedirect('/')


#This Class will Edit and update 

class UserupdateView(View):
    def get(self,request,id):
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        return render(request,'enroll/updatestudent.html',{'form':fm})
    def post(self,request,id):
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if  fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')        






# def update_data(request,id):
#     if request.method =='POST':
#         pi=Student.objects.get(pk=id)
#         fm=StudentRegistration(request.POST,instance=pi)
#         if  fm.is_valid():
#             fm.save()
#     else:
#         pi=Student.objects.get(pk=id)
#         fm=StudentRegistration(instance=pi)

#     return render(request,'enroll/updatestudent.html',{'form':fm})




#This Class will Delate iteam
class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        Student.objects.get(pk=del_id).delete()
        
        return super().get_redirect_url(*args, **kwargs)




# def delete_data(request, id):
#     if request.method=='POST':
#         pi=Student.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')

