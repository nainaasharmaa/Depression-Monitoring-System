from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def healing(request):
    return render(request, 'healing.html', {})

def about(request):
    return render(request, 'about.html', {})

def login(request):
    return render(request, 'login.html', {})

def survey(request):
    return render(request, 'survey.html', {})

def ContactUs(request):
    return render(request, 'ContactUs.html', {})

def session1(request):
    return render(request, 'session1.html', {})

def session2(request):
    return render(request, 'session2.html', {})

def session3(request):
    return render(request, 'session3.html', {})

def signup(request):
    return render(request, 'signup.html', {})