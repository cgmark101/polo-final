from django import forms 
from .models import Productos

class ArticuloForm(forms.ModelForm): 
    class Meta: 
        model = Productos 
        fields = ['titulo', 'imagen', 'descripcion', 'precio', 'categoria'] 