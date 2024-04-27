from django.http import HttpRequest, request, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Candidate

def new(request):
    return render(request, "new.html")

def create(request):
    if request.method == "POST":
        candidate = Candidate(
            name=request.POST["name"],
            age=request.POST["age"],
            party=request.POST["party"]
        )

        candidate.save()
        candidates = Candidate.objects.all()
        return render(request, "candidates/index.html", { "candidates": candidates })
    return HttpResponseRedirect(reverse("vote_candidates:new"))