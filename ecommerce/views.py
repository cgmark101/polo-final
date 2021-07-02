from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import ArticuloForm
from django.contrib import messages
from .models import Categorias, Productos

def acerca(request):
    titulo = "Acerca"
    return render (request=request, template_name="acerca.html", context={"titulo":titulo})

def contacto(request):
    titulo = "Contacto"
    return render (request=request, template_name="contacto.html", context={"titulo":titulo})

def home(request):
	titulo = 'Inicio'
	cat = Categorias.objects.all()
	last_articulo = Productos.objects.all().order_by('-id')[:3]
	restantes_articulos = Productos.objects.all().order_by('-id')[3:10]

	return render (
		request=request, 
		template_name='home.html', 
		context={
			'titulo':titulo, 
			'cat':cat, 
			'data': last_articulo,
			'data2': restantes_articulos
			}
		)

def all_products(request, producto_id):
    articulo = Productos.objects.all()
    return render(request, 'productos.html', {'articulo':articulo})

def detail_products(request, producto_id):
	cat = Categorias.objects.all()
	detalle=Productos.objects.get(id=producto_id)
	return render(request, 'productos.html', {'producto':  detalle, 'cat':cat})

def category(request):
	cat = Categorias.objects.all()
	return render(request, 'categorias.html', {'cat':cat})

def detail_category(request, cat):
	detalle = Categorias.objects.all()
	cat1 = Categorias.objects.all()
	articulos = Productos.objects.filter(categoria__categoria__contains=cat)	

	return render(request, 'categoria.html', {'cat_detalle':detalle, 'articulos':articulos, 'cat':cat1, })

def search(request):
	titulo = "Busqueda"
	cat = Categorias.objects.all()
	searched = request.POST['searched']
	busqueda = Productos.objects.filter(titulo__contains=searched)

	if not busqueda:
		print('not')
		return render (request=request, template_name="search.html", context={"titulo":titulo, 'no_encontrado':f'Articulo {searched} no encontrado', 'cat':cat})
		
	else:
		if request.method == 'POST':
			print('post')
			return render (request=request, template_name="search.html", context={"titulo":titulo, "searched":searched, "busqueda":busqueda, 'cat':cat})
		if request.method == 'GET':
			print('ok')
			return render (request=request, template_name="search.html", context={"titulo":titulo, 'cat':cat})
			
@login_required		
def add_article(request, *args, **kwargs):	
	if request.method == 'POST':
		form = ArticuloForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Articulo agregado' )
			return redirect('home')
		messages.error(request, 'Error')
	formulario = ArticuloForm
	titulo = 'Agregar'
	return render (
		request=request, 
		template_name='crear-articulo.html', 
		context={'agregar':formulario, 'titulo':titulo})