from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("", include("vote_candidates.urls")),
    path("candidate/<id>", views.show, name="show"),
    path("candidate/<id>/edit", views.edit, name="edit"),
    path("candidate/<id>/update", views.update, name="update"),
]
