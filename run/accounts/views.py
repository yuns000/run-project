from django.http import HttpResponse
from django.shortcuts import redirect, render


def login(request) -> HttpResponse:
    return render(request, 'accounts/login/login.html')

def account_creation(request) -> HttpResponse:
    return render(request, 'accounts/account_creation/account_creation.html')