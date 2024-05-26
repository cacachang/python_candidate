from django.http import HttpRequest, request, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Candidate
from candidates.forms import CandidateForm

def new(request):
    form = CandidateForm()
    return render(request, "new.html", { "form": form})

def create(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)

        if form.is_valid():
            candidate = Candidate(**form.cleaned_data)
            candidate.save()

        candidates = Candidate.objects.all()
        return render(request, "candidates/index.html", { "candidates": candidates })
    return HttpResponseRedirect(reverse("vote_candidates:new"))
