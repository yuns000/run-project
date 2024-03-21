# Create your views here.
# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, World!")