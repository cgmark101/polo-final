from django.contrib import admin
from ecommerce.models import Categorias, Productos, Carrito

# Register your models here.

admin.site.register(Categorias)
admin.site.register(Productos)
admin.site.register(Carrito)