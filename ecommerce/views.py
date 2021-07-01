from django.shortcuts import render
from .models import Categorias

def acerca(request):
    titulo = "Acerca"
    return render (request=request, template_name="acerca.html", context={"titulo":titulo})

def contacto(request):
    titulo = "Contacto"
    return render (request=request, template_name="contacto.html", context={"titulo":titulo})

