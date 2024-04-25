from django.http import HttpRequest
from django.shortcuts import render

def new(request):
    return render(request, "new.html")

def create(request):
    
    return render(request, "create.html")