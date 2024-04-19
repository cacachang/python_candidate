from django.http import HttpRequest
from django.shortcuts import render

def new(request):
    return render(request, "new.html")