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

]