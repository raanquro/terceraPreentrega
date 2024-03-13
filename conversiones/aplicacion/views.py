from django.shortcuts import render
from .models import * 
from .forms import *
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

#____________________________________________Forms

def clienteForm(request):
    if request.method == "POST":
    #Esta parte es para cuando el formulario ingresa por 2da o 3ra o... vez
        miForm = ClienteForm(request.POST)    
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_placa = miForm.cleaned_data.get("placa")
            cliente_marca = miForm.cleaned_data.get("marca")
            cliente_modelo = miForm.cleaned_data.get("modelo")
            cliente_visitas = miForm.cleaned_data.get("visitas")
            
            cliente = Cliente(nombre = cliente_nombre,
                              apellido = cliente_apellido,
                              placa = cliente_placa,
                              marca = cliente_marca,
                              modelo = cliente_modelo,
                              visitas = cliente_visitas,
                              )
            cliente.save()
            
            contexto = {'clientes': Cliente.objects.all()}
            return render (request,"aplicacion/clientes.html",contexto)
    else:
        miForm = ClienteForm()
    return render(request, "aplicacion/clienteForm.html", {"form":miForm})


def asesorForm(request):
    if request.method == "POST":
    #Esta parte es para cuando el formulario ingresa por 2da o 3ra o... vez
        miForm = AsesorForm(request.POST)    
        if miForm.is_valid():
            asesor_nombre = miForm.cleaned_data.get("nombre")
            asesor_apellido = miForm.cleaned_data.get("apellido")
            asesor_sede = miForm.cleaned_data.get("sede")
            asesor_email = miForm.cleaned_data.get("email")
            
            asesor = Asesor(nombre = asesor_nombre,
                            apellido = asesor_apellido,
                            sede = asesor_sede,
                            email = asesor_email,
                              )
            asesor.save()

            contexto = {'asesores': Asesor.objects.all()}
            return render (request,"aplicacion/asesores.html",contexto)
    else:
        miForm = AsesorForm()
    return render(request, "aplicacion/asesorForm.html", {"form":miForm})


def homologacionForm(request):
    if request.method == "POST":
    #Esta parte es para cuando el formulario ingresa por 2da o 3ra o... vez
        miForm = HomologacionForm(request.POST)    
        if miForm.is_valid():
            homologacion_marca = miForm.cleaned_data.get("marca")
            homologacion_modelo = miForm.cleaned_data.get("modelo")
            homologacion_tipo_conversion = miForm.cleaned_data.get("tipo_conversion")
            homologacion_equipo_gas = miForm.cleaned_data.get("equipo_gas")
            
            homologacion = Homologacion(marca = homologacion_marca,
                                        modelo = homologacion_modelo,
                                        tipo_conversion = homologacion_tipo_conversion,
                                        equipo_gas = homologacion_equipo_gas,
                            )
            homologacion.save()

            contexto = {'homologaciones': Homologacion.objects.all()}
            return render (request,"aplicacion/homologaciones.html",contexto)
    else:
        miForm = HomologacionForm()
    return render(request, "aplicacion/homologacionForm.html", {"form":miForm})

#_______________ Funciones para buscar en cada una de las tablas de la base de datos.
#_________________________________________Buscar Cliente
def buscarCliente (request):
    return render(request, "aplicacion/buscarClientes.html")

def encontrarCliente(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {"clientes":clientes}
        return render (request,"aplicacion/clientes.html",contexto)

    contexto = {'clientes':Cliente.objects.all()}
    return render (request, "aplicacion/clientes.html")

#_________________________________________Buscar Asesor
def buscarAsesor (request):
    return render(request, "aplicacion/buscarAsesores.html")

def encontrarAsesor(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        asesores = Asesor.objects.filter(nombre__icontains=patron)
        contexto = {"asesores":asesores}
        return render (request,"aplicacion/asesores.html",contexto)

    contexto = {'asesores':Asesor.objects.all()}
    return render (request, "aplicacion/asesores.html")

#_________________________________________Buscar Homologacion
def buscarHomologacion (request):
    return render(request, "aplicacion/buscarHomologaciones.html")

def encontrarHomologacion(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        homologaciones = Homologacion.objects.filter(marca__icontains=patron)
        contexto = {"homologaciones":homologaciones}
        return render (request,"aplicacion/homologaciones.html",contexto)

    contexto = {'homologaciones':Homologacion.objects.all()}
    return render (request, "aplicacion/homologaciones.html")