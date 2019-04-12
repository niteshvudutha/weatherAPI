from django.urls import path
from . import views
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
                           