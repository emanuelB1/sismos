from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_sismos, name="index"),
    path("busqueda/", views.busqueda, name="busqueda"),
]
