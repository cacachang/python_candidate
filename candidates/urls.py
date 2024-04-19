from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include("vote_candidates.urls")),
    path('', views.index),
    path('admin/', admin.site.urls),
]
