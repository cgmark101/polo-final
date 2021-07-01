from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("acerca", views.acerca, name="acerca"),
    path("contacto", views.contacto, name="contacto"),
]
