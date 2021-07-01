from django.shortcuts import render, redirect
from .forms import Nuevousuario
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from ecommerce.models import *

def home(request):
    titulo = "Inicio"
    cat = Categorias.objects.all()
    articulo = Productos.objects.all()
    print(cat)
    return render (
		request=request, 
		template_name="home.html", 
		context={
			"titulo":titulo, 
			"cat":cat, 
			"articulo":articulo
			}
		)

def products(request):
    cat = Categorias.objects.all()
    articulo = Productos.objects.all()
    return render(request, 'productos.html', {'articulo':articulo})

def register_request(request):	
	if request.method == "POST":
		form = Nuevousuario(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect("home")
		messages.error(request, "Registro no exitoso. Informacion invalida.")
	form = Nuevousuario
	titulo = "Registro"
	return render (
		request=request, 
		template_name="register.html", 
		context={
			"register_form":form, 
			'titulo':titulo
			}
		)

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Estas autenticado como {username}.")
				return redirect("home")
			else:
				messages.error(request,"Usuario o contrasena incorrecta.")
		else:
			messages.error(request,"Usuario o contrasena incorrecta.")
	form = AuthenticationForm()
	titulo = "Login"
	return render(
		request=request, 
		template_name="login.html", 
		context={
			"login_form":form, 
			'titulo':titulo
			}
		)

def logout_request(request):
	logout(request)
	messages.info(request, "Logout exitoso.") 
	return redirect("home")
