from django import forms


class CursoForm(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
class EstudiantesForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    foto = forms.ImageField(required=False)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    
class ProfesoresForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    
class Buscar(forms.Form):
    camada = forms.CharField(max_length=20)