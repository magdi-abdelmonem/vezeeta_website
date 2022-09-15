from dataclasses import fields
from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class Sign_Up(UserCreationForm):
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

        widgets = {

        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        'password1':forms.TextInput(attrs={'class':'form-control'}),
        'password2':forms.TextInput(attrs={'class':'form-control'}),
    }


class UpdateInformForm(UserChangeForm):                
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password',"is_staff","is_active","date_joined","last_login")


        widgets = {

        'username'   :forms.TextInput(attrs={'class':'form-control'}),
        'first_name' :forms.TextInput(attrs={'class':'form-control'}),
        'last_name'  :forms.TextInput(attrs={'class':'form-control'}),
        'email'      :forms.TextInput(attrs={'class':'form-control'}),
        'password'   :forms.PasswordInput(attrs={'class':'form-control'}),
        'is_staff'   :forms.CheckboxInput(attrs={'class':'form-check'}),
        "is_active"  :forms.CheckboxInput(attrs={'class':'form-check'}),
        "date_joined":forms.TextInput(attrs={'class':'form-control'}),
        "last_login" :forms.TextInput(attrs={'class':'form-control'}),

    }  



class add_doctor(forms.ModelForm):                
    class Meta:
        model=Profile
        fields=('name','Specialization','governorate','address','phone','who_i','price','image','facebook','twitter','gmail','gender')

        widgets = {

        'name' :forms.TextInput(attrs={'class':'form-control'}),
        'Specialization':forms.Select(choices=Specializations ,attrs={'class':'form-control'}),
        'governorate':forms.Select(choices=governorate ,attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'phone' :forms.TextInput(attrs={'class':'form-control'}),
        'who_i' :forms.TextInput(attrs={'class':'form-control'}),
        'price' :forms.TextInput(attrs={'class':'form-control'}),
        #'image' :forms.ImageField(attrs={'class':'form-control'}),
        'facebook' :forms.TextInput(attrs={'class':'form-control'}),
        'twitter' :forms.TextInput(attrs={'class':'form-control'}),
        'gmail' :forms.TextInput(attrs={'class':'form-control'}),
        'gender' :forms.Select(attrs={'class':'form-control'}),
    } 
        


class loginform(forms.ModelForm):
    username=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','password')



    

class UpdateForm(forms.ModelForm):                
    class Meta:
        model=Profile
        fields=('name','Specialization','governorate','address','phone','who_i','price','image','facebook','twitter','gmail','gender')

        widgets = {

        'name' :forms.TextInput(attrs={'class':'form-control'}),
        'Specialization':forms.Select(choices=Specializations ,attrs={'class':'form-control'}),
        'governorate':forms.Select(choices=governorate ,attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'phone' :forms.TextInput(attrs={'class':'form-control'}),
        'who_i' :forms.TextInput(attrs={'class':'form-control'}),
        'price' :forms.TextInput(attrs={'class':'form-control'}),
        'image' :forms.TextInput(attrs={'class':'form-control'}),
        'facebook' :forms.TextInput(attrs={'class':'form-control'}),
        'twitter' :forms.TextInput(attrs={'class':'form-control'}),
        'gmail' :forms.TextInput(attrs={'class':'form-control'}),
        'gender' :forms.Select(attrs={'class':'form-control'}),
    } 



class commentform(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('rating','comment_space',)

        widgets = {
        'rating':forms.Select(choices=ratings ,attrs={'class':'form-control'}),
        'comment_space':forms.Textarea(attrs={'class':'form-control'}),
        
    } 