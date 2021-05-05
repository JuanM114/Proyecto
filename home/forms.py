from django import forms
from .models import *
class contacto_form (forms.Form):
    correo = forms.EmailField(widget = forms.TextInput())
    titulo = forms.CharField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea())
    
class agregar_producto_form(forms.Form):
    class Meta:
        modelo = Producto
        field ='__all__'
        
class agregar_marca_form(forms.Form):
    class Meta:
        modelo = Producto
        field ='__all__'        
        