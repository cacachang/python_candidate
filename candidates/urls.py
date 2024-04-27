from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include("vote_candidates.urls")),
    path('candidates/index', views.index, name='index'),
]
