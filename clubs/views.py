from django.shortcuts import render, redirect
from accounts.models import UserAccount
from django.contrib.auth import login, logout, authenticate
from clubs.models import ClubAccount
from django.http import HttpResponse


def index(request):
    return render(request, 'clubs/index.html')

def events(request):
    return render(request, 'clubs/events.html')

def recruitments(request):
    return render(request, 'clubs/recruitments.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        verified = UserAccount.objects.get(email=email)
        if user is not None and verified.club_verification:
            login(request, user)
            return HttpResponse('Club Hub')
        else:
            return HttpResponse('Club not registered')
        
    return render(request, 'clubs/login.html')

def Logout(request):
    logout(request)
    return redirect('/login')



            
