from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("juan", views.juan, name="juan"),
    
]