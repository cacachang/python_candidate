from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include("vote_candidates.urls")),
    path('<id>', views.show, name='show'),
]
