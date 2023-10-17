from django.shortcuts import redirect, render
from django.contrib.auth import login,logout ,authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .decorators import notLoggedUser ,allowedUsers

from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

import requests
from django.conf import settings

#nafs dawar dyal LoginRequiredMixin f class
@login_required(login_url='login')
def ProfileView(request):
    return render(request,'profile.html')


def HomeView(request):
    return render(request,'home.html')

@login_required(login_url='login')
@allowedUsers(allowedUsers=['admin'])
def AdminView(request):
    return render(request,'admin.html')
    group =Group.objects.get(name='admin')
    user.groups.add(group)

# @notLoggedUser
# @allowedUsers(allowedUsers=['client'])
# def sign_up(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'GET':
#             form = RegisterForm()
#             return render(request, 'users/register.html',{'form': form})    
#         if request.method == 'POST':
#             form = RegisterForm(request.POST) 
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 user.username = user.username.lower()
#                 user.save()
#                 messages.success(request, 'You have signed up successfully.')
#                 login(request, user)
#                 return redirect('profile')
#             else:
#                 return render(request, 'users/register.html',{'form': form})

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            form = RegisterForm()
            return render(request, 'users/register.html', {'form': form})
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            if response.json()['success']:
                if form.is_valid():
                    user = form.save(commit=False)
                    user.username = user.username.lower()
                    user.save()
                    messages.success(request, 'You have signed up successfully.')
                    login(request, user)
                    return redirect('profile')
            else:
                form.add_error(None, 'Invalid reCAPTCHA response.')
            return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            form = LoginForm()
            return render(request, 'users/login.html', {'form': form})
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have logged in successfully.')
                    return redirect('profile')
                else:
                    messages.error(request, 'Invalid username or password.')
                    return render(request, 'users/login.html', {'form': form})
            else:
                return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')




