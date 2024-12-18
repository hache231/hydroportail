from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import LoginForm, UserForm
from accounts.models import visitor


def  index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('map')
        else:
            return HttpResponse('Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def sign_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            email=request.POST['email']
        )
        user.save()
        username=request.POST['username']
        password=request.POST['password']
        # Create a Visitor entry
        visitor.objects.create(
            user=user,
            middlename=request.POST['middlename'],
            sex=request.POST['sex'],
            birthday=request.POST['birthday'],
            fonction=request.POST['fonction'],
        )
        
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('map')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')