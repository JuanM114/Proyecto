from rest_framework import serializer
from home.models import *

class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url' ,'nombre', 'descripcion', 'status', 'foto', 'precio', 'marca', 'categorias',)
        
class marca_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url' ,'nombre', 'descripcion', 'status', 'foto', 'precio', 'marca', 'categorias',)        

class categorias_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorias
        fields = ('url' ,'nombre', 'descripcion', 'status', 'foto', 'precio', 'marca', 'categorias',)   