from django.urls import path
from .views import *

urlpatterns = [
path('about/',about_view, name='about_view'),
path('contacto/',contacto_view, name='contacto_view'),
path('servicios/',servicios_view, name='servicios_view'),
path('productos/',productos_view, name='productos_view'),
path('marca/',marca_view, name='marca_view'),
path('categoria/',categoria_view, name='categoria_view'),
path('agregar_producto/', agregar_producto_view, name='agregar_producto_view'),
path('agregar_marca/', agregar_marca_view, name='agregar_marca_view'),
path('eliminar_producto/<int:id_prod>', eliminar_producto_view, name='eliminar_producto_view'),
path('editar_producto/<int:id_prod>', editar_producto_view, name='editar_producto_view'),
]