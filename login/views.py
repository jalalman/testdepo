from django.shortcuts import render ,redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.

def login(request):

    return render(request,"login.html")


def createUser(request):
    if request.method=="POST":
        errors=User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            models.addUser(request.POST)
    return redirect ('/')

def loginConfirm(request):
    if request.method=="POST":
        email=User.objects.filter(email=request.POST['username']).first()
        if not email:
            email=User.objects.filter(username=request.POST['username']).first()

        if email :
            if bcrypt.checkpw(request.POST['password'].encode(),email.password.encode()) or bcrypt.checkpw(request.POST['password'].encode(),email.password.encode()):
                request.session['username']=email.username
                request.session['id']=int(email.id)
                

                return redirect('/showshome')
            else:

                messages.error(request, "Invalid email/username or password")
                return redirect('/')



    messages.error(request, "Invalid email/username or password")
    return redirect ('/')

def showshome(request):


    return redirect('tvshowapp:allshows')