from http.client import HTTPResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy ,reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from .models import Profile,Comment
from .form import *
from django.contrib.auth import authenticate,login

    
def doctor_list(request):
    doctors=Profile.objects.all()
    return render(request,'doctors_list.html',{'doctors': doctors,})


def search_doctors(request):
    if request.method=="POST":
        searched=request.POST['searched']
        Specialization=request.POST['Specialization']
        address=request.POST['governorate']
        data=Profile.objects.filter(name__contains=searched, Specialization__contains=Specialization, governorate=governorate)
        
        return render(request,'search_doctors.html',{
            'searched':searched,
            'Specialization':Specialization,
            'governorate': governorate,
            'data':data
        })


    else:
        return render(request,'search_doctors.html',{})



def doctor_profile(request,pk):
    #doctor_profile=Profile.objects.get(pk=pk)
    doctor_profile=get_object_or_404(Profile,pk=pk)
    return render(request,'doctor_profile.html',{'doctor_profile':doctor_profile})


class commentview(CreateView):
    model=Comment
    form_class=commentform
    template_name=('comment_page.html')
    
    def form_valid(self, form):                     #المعادلة دي انه يفهم تلقائي اسم الطبيب اللي انا هعلق عليه 
        form.instance.profile_id=self.kwargs['pk']         
        return super().form_valid(form)

    success_url =reverse_lazy('doctor_list')    
    

def log(request):
    if request.method =='POST':
        form=loginform()
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('doctor_list')
    else:
        form=loginform()
    return render(request,'login.html',{'form':form,})




class Register(CreateView):
    model=User
    form_class=Sign_Up
    template_name=('register.html')
    success_url =reverse_lazy('doctor_list')



class Add_doctor(CreateView):
    model=Profile
    form_class=add_doctor
    template_name=('add_doctor.html')
    success_url=reverse_lazy('doctor_list')



class Update_profile(UpdateView):
    model=Profile
    form_class=UpdateForm
    template_name=('update_profile.html')
    success_url =reverse_lazy('doctor_list')



class Update_profile_inform(UpdateView):
    model=User
    form_class=UpdateInformForm
    template_name=('update_inform.html')
    success_url =reverse_lazy('doctor_list')


