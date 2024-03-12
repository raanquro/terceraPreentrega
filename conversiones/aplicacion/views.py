from django.shortcuts import render
from .models import * 

# Create your views here.

def home(request):
    return render (request,"aplicacion/index.html")

def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render (request,"aplicacion/clientes.html",contexto)

def asesores(request):
    contexto = {'asesores': Asesor.objects.all()}
    return render (request,"aplicacion/asesores.html",contexto)

def homologaciones(request):
    contexto = {'homologaciones': Homologacion.objects.all()}
    return render (request,"aplicacion/homologaciones.html",contexto)