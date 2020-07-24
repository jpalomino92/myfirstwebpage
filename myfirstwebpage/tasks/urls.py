from django.urñs import path

from . import views

urlspatterns = [
    path("", views.index,name = "index")
]