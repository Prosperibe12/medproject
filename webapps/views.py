from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

# index function
def index_view(request):
    
    banner = Banner.objects.all()
    context = {
        'banner': banner,
        'Title': 'Home Page'
    }
    return render(request, 'webapps/index.html', context)

# register function
def register_view(request):
    
    # prevent authenicated users from going register page when logged in
    if request.user.is_authenticated:
        messages.warning(request, 'Already Logged In')
        redirect('user:dashboard')
    
    form = PatientForm
    # process registeration form 
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password1 = form.cleaned_data.get('password2')
            
            if password != password1:
                messages.warning(request, 'Password do not Match')
                return redirect('web:register')
            
            user = User.objects.create_user(username, email, password)
            form = form.save(commit=False)
            form.user = user
            form.save()
            messages.success(request, 'Registered Successfully')
            return redirect('web:login')
        else:
            messages.warning(request, 'Kindly Check your Form')
    
    context = {
        'Title': "Register Page",
        'form':form
    }
    return render(request, 'webapps/register.html', context)

# login view
def login_view(request):
    
    # prevent authenicated users from going login page when logged in
    if request.user.is_authenticated:
        messages.warning(request, 'Already Logged In')
        redirect('user:dashboard')
    
    # process login
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged In Successfully')
            return redirect('user:dashboard')
        else:
            messages.warning(request, 'Invalid Username or Password')
    
    context = {
        'Title': "Login Page"
    }
    return render(request, 'webapps/login.html', context)

# function to logout user
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('web:login')
