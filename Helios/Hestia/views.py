from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import tablib
import csv
from import_export import resources
from Icarus import models

# Create your views here.
def userlogin(request):
    if request.method=='POST':
        huser = authenticate(username=request.POST['username'], password=request.POST['password'])

        if huser is not None:
            login(request, huser)
            return redirect('home')

        else:
            errormsg = 'Username or password invalid.'
            return render(request, 'Hestia/login.html', {'errormsg':errormsg})
    else:
        return render(request, 'Hestia/login.html')

def userlogout(request):
    logout(request)
    return redirect('home')

def users_all(request):
    husers = User.objects.all()
    return render(request, 'Hestia/users_all.html', {'husers':husers})

def users_new(request):
    if request.method == "POST":
        if request.POST['username'] and request.POST['password'] and request.POST['passwordCom']:
            if request.POST['password'] == request.POST['passwordCom']:
                try:
                    huser = User.objects.get(username=request.POST['username'])
                    errormsg = 'Username already in use.'
                    email = request.POST['email']
                    return render(request, 'Hestia/users_new.html', {'errormsg':errormsg, 'email':email})

                except User.DoesNotExist:
                    User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                    return redirect('users_all')
            else:
                errormsg = 'Passwords don\'t match.'
                username = request.POST['username']
                email = request.POST['email']
                return render(request, 'Hestia/users_new.html', {'errormsg':errormsg, 'username':username, 'email':email})
        else:
            errormsg = 'All fields are required.'
            username = request.POST['username']
            email = request.POST['email']
            return render(request, 'Hestia/users_new.html', {'errormsg':errormsg, 'username':username, 'email':email})
    else:
        return render(request, 'Hestia/users_new.html')

def users_detail(request, pk):
    huser = User.objects.get(pk=pk)
    tasks = models.Tasks.objects.filter(assigned_to=huser.pk)
    return render(request, 'Hestia/users_detail.html', {'huser':huser, 'tasks':tasks})

def users_edit(request, pk):
    huser = User.objects.get(pk=pk)
    if request.method == "POST":
        if request.POST['username'] and request.POST['password'] and request.POST['passwordCom']:
            if request.POST['password'] == request.POST['passwordCom']:
                huser.username = request.POST['username']
                huser.email = request.POST['email']
                huser.password = request.POST['password']
                huser.save()
                return redirect('users_detail', pk=user.pk)
            else:
                errormsg = 'Passwords don\'t match.'
                username = request.POST['username']
                email = request.POST['email']
                return render(request, 'Hestia/users_edit.html', {'huser':huser, 'errormsg':errormsg, 'username':username, 'email':email})
        else:
            errormsg = 'All fields are required.'
            username = request.POST['username']
            email = request.POST['email']
            return render(request, 'Hestia/users_edit.html', {'huser':huser, 'errormsg':errormsg, 'username':username, 'email':email})
    else:
        username = huser.username
        email = huser.email
    return render(request, 'Hestia/users_edit.html', {'huser':huser, 'username':username, 'email':email})
