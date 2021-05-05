from django.shortcuts import render
from .forms import *
# Create your views here.
def about_view(request):
    return render(request,'about.html')
 
def contacto_view(request):
    email = ""
    title = ""
    text = ""
    info_enviado = False
    if request.method == 'POST':
       formulario = contacto_form(request.POST) 
    if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['correo']
            title = formulario.cleaned_data['titulo']
            text = formulario.cleaned_data['texto']
    else:
        formulario = contacto_form()
    return render(request,'contacto.html',locals())

def servicios_view(request):
    return render(request,'servicios.html',locals())

def productos_view(request):
   
    return render(request,'productos.html',locals())

def marca_view(request):
       
    return render(request,'marca.html',locals())

def categoria_view(request):
       
    return render(request,'categoria.html',locals())

def agregar_producto_view(request):
    
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/productos/')
    else:         
        formulario =agregar_producto_form()
    return render(request,'agregar_producto.html', locals())

def agregar_marca_view(request):
    if request.method == 'POST':
        formulario = agregar_marca_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/marca/')
    else:         
        formulario =agregar_marca_form()
    return render(request,'agregar_marca.html', locals())


def ver_producto_view(request, id_prod):
    detalle = Producto.objects.get(id= id_prod)
    #get_or_404
    return render(request,'ver_producto.html', locals())


def eliminar_producto_view(request, id_prod):
    odjeto = Porducto.objects.get(id=id_prod)
    objeto.delete()
    return redirect('/productos.html', locals())


def editar_producto_view(request, id_prod):
    objeto = Producto.objects.get(id=id_prod)
    if request.metthod == 'POST':
        formulaio = agregar_producto_form(reques.POST, request.FILES, instance= objeto)
        if fomulario_is.valid():
            objeto=formulario.save()
            return redirect('/ver_producto/')
    else:    
        
         formulario = agregar_producto_form(instance= objeto)
    return render('agregar_producto.html', locals())