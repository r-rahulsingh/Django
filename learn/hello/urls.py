from django.urls import path

# from hello import views
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("name",views.name, name="name ")
]

