from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('clientes/',clientes,name="clientes"),
    path('asesores/',asesores,name="asesores"),
    path('homologaciones/',homologaciones,name="homologaciones"),

]