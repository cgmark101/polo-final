from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorias(models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.categoria
    class Meta:
        verbose_name = 'Categoria'

class Productos(models.Model):
    titulo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='static/img/photos', max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = 'Articulo'

class Carrito(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    list = models.ManyToManyField(Productos, blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.list

    class Meta:
        verbose_name_plural = 'Carrito'
    