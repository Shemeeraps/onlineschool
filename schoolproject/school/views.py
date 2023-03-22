from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from . forms import updateprofile
from tkinter import *


# Create your views here.
def demo(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
        confirm_password=request.POST['password2']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME NOT AVAILABLE")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password not match")
    return render(request,"registration.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('detail')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
def detail(request):
    return render(request,'detail.html')
def update(request):
    return render(request,'contact.html')

def updateform(request):
    if request.method == 'POST':
        messages.info(request,"Profile Updated Successfully!!")
        return redirect('update')
