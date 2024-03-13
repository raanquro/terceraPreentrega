from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('clientes/',clientes,name="clientes"),
    path('asesores/',asesores,name="asesores"),
    path('homologaciones/',homologaciones,name="homologaciones"),

    path('cliente_form/',clienteForm,name="cliente_form"),
    path('asesor_form/',asesorForm,name="asesor_form"),
    path('homologacion_form/',homologacionForm,name="homologacion_form"),

#____________________________________Busqueda
    path('buscar_clientes/',buscarCliente,name="buscar_clientes"),
    path('encontrar_clientes/',encontrarCliente,name="encontrar_clientes"),

    path('buscar_asesores/',buscarAsesor,name="buscar_asesores"),
    path('encontrar_asesores/',encontrarAsesor,name="encontrar_asesores"),
        
    path('buscar_homologaciones/',buscarHomologacion,name="buscar_homologaciones"),
    path('encontrar_homologaciones/',encontrarHomologacion,name="encontrar_homologaciones"),

]