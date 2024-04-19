from django.contrib import admin
from django.urls import path
from . import views

app_name = 'vote_candidates'

urlpatterns = [
    path('vote_candidates/new', views.new, name="new"),
]
