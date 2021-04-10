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
