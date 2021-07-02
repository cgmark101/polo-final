from django.shortcuts import render
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

	# contador = 0
	# data = []
	# for i in reversed(articulo):
	# 	print(i)
	# 	data.append(i)
	# 	if contador == 2:
	# 		break
	# 	contador = contador + 1
	# print(data)
	#print(cat)
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
    detalle=Productos.objects.get(id=producto_id)
    return render(request, 'productos.html', {'producto':  detalle})

def category(request):
	cat = Categorias.objects.all()
	return render(request, 'categorias.html', {'cat':cat})

def detail_category(request, cat):
	detalle = Categorias.objects.all()
	# data_cat = []
	# data_filter = []
	# for i in detalle:
	# 	data_cat.append(i.categoria)
	# print(data_cat)
	articulos = Productos.objects.filter(categoria__categoria__contains=cat)
	# for i in articulos:
	# 	data_filter.append(i)
	# if data_filter in data_cat:
	# 	pass
	# print(data_filter)
	

	return render(request, 'categoria.html', {'cat_detalle':detalle, 'articulos':articulos})

def search(request):
	titulo = "Busqueda"
	cat = Categorias.objects.all()
	searched = request.POST['searched']
	busqueda = Productos.objects.filter(titulo__contains=searched)
	no_encontrado = f'Articulo {searched} no encontrado'
	if not busqueda:
		return render (request=request, template_name="search.html", context={"titulo":titulo, 'no_encontrado':no_encontrado})
	else:
		if request.method == 'POST':
			return render (request=request, template_name="search.html", context={"titulo":titulo, "searched":searched, "busqueda":busqueda})
		if request.method == 'GET':
			return render (request=request, template_name="search.html")
		