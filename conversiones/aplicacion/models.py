from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    visitas = models.CharField(max_length=50)

class Asesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sede = models.CharField(max_length=50)
    email = models.EmailField()

class Homologacion(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo_conversion = models.CharField(max_length=50)
    equipo_gas = models.CharField(max_length=50)
