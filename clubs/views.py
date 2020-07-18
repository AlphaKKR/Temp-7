from django.shortcuts import render, redirect
from accounts.models import UserAccount
from django.contrib.auth import login, logout, authenticate



def index(request):
    return render(request, 'clubs/index.html')

def events(request):
    return render(request, 'clubs/events.html')

def recruitments(request):
    return render(request, 'clubs/recruitments.html')


            
