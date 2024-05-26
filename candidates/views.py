from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from vote_candidates import models
from .forms import CandidateForm


def index(request):
    candidates = models.Candidate.objects.all()
    return render(request, "candidates/index.html", {"candidates": candidates})


def show(request, id):
    try:
        candidate = models.Candidate.objects.get(id=id)
    except:
        return HttpResponse("沒有這號人物", status=404)

    return render(request, "candidates/show.html", {"candidate": candidate})


def edit(request, id):
    candidate = get_object_or_404(models.Candidate, id=id)
    form = CandidateForm(candidate.__dict__)

    return render(
        request, "candidates/edit.html", {"form": form, "candidate": candidate}
    )


def update(request, id):
    candidate = get_object_or_404(models.Candidate, id=id)

    if request.method == "POST":
        form = CandidateForm(request.POST)

        if form.is_valid():
            candidate.name = form.cleaned_data["name"]
            candidate.party = form.cleaned_data["party"]
            candidate.age = form.cleaned_data["age"]
            candidate.save()

            return redirect("show", id=id)

    form = CandidateForm(candidate.__dict__)
    return render(
        request,
        "candidates/edit.html",
        {"form": form, "candidate": candidate},
    )
