from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import User


def login(request) -> HttpResponse:
    return render(request, 'accounts/login/login.html')

def account_creation(request) -> HttpResponse:
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        location = request.POST.get('location')
        
        if User.objects.filter(email=email).exists():
            message = 'Email already exists'
            success = False
        else:
            User.create_user(email, password, username, location)
            message = 'success'
            success = True
        return JsonResponse({'success': success, 'message' : message})
    elif request.method == 'GET':
        return render(request, 'accounts/account_creation/account_creation.html')