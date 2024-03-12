from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    apellido = forms.CharField(max_length=50,required=True)
    placa = forms.CharField(max_length=10,required=True)
    marca = forms.CharField(max_length=50,required=True)
    modelo = forms.CharField(max_length=50,required=True)
    visitas = forms.CharField(max_length=50,required=True)

class AsesorForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    apellido = forms.CharField(max_length=50,required=True)
    sede = forms.CharField(max_length=50,required=True)
    email = forms.EmailField()

class HomologacionForm(forms.Form):
    marca = forms.CharField(max_length=50,required=True)
    modelo = forms.CharField(max_length=50,required=True)
    tipo_conversion = forms.CharField(max_length=50,required=True)
    equipo_gas = forms.CharField(max_length=50,required=True)
