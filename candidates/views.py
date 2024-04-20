from django.shortcuts import render
from django.http import HttpResponse
from vote_candidates import models

def index(request):
    candidates = models.Candidate.objects.all()
    return render(request, "candidates/index.html", { "candidates": candidates } )

def show(request, id):
    try:
        candidate = models.Candidate.objects.get(id = id)
    except:
        return HttpResponse("沒有這號人物", status=404)

    return render(request, "candidates/show.html", { "candidate": candidate })
