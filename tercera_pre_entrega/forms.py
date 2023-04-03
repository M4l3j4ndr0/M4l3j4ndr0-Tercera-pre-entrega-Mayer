from django import forms

class NotasForm (forms.Form):
    alumno = forms.CharField(max_length=100)
    materia = forms.CharField(max_length=100)
    fecha_parcial = forms.DateField()
    nota_parcial = forms.CharField(max_length=2)

class BuscarPersonasForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)