from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Estudiantes, Profesores
from .forms import CursoForm, EstudiantesForm, ProfesoresForm, Buscar
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def padre(req):
    return render(req, 'appproyecto/padre.html')

@login_required
def curso(req):
    return render(req, 'appproyecto/curso.html')

@login_required
def cursoform(request):
    if request.method == "POST":
        miFormulario = CursoForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(curso=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppProyecto/padre.html")
    else:
        miFormulario = CursoForm()
    return render(request, "AppProyecto/cursoform.html", {"miFormulario": miFormulario})

@login_required
def profesores(req):
    return render(req, 'appproyecto/profesores.html')

@login_required
def profesoresform(request):
    if request.method == "POST":
        miFormulario = ProfesoresForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesores = Profesores(nombreapellidoProf=informacion["nombre"], email=informacion["email"], profesion=informacion["profesion"])
            profesores.save()
            return render(request, "AppProyecto/padre.html")
    else:
        miFormulario = ProfesoresForm()
    return render(request, "AppProyecto/profesoresform.html", {"miFormulario": miFormulario})

@login_required
def estudiantes(req):
    return render(req, 'appproyecto/estudiantes.html')

@login_required
def estudiantesform(request):
    if request.method == "POST":
        miFormulario = EstudiantesForm(request.POST, request.FILES)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiantes = Estudiantes(nombreapellidoEst=informacion["nombre"], email=informacion["email"])
            estudiantes.save()
            if informacion.get("foto"):
                estudiantes.foto.save(foto=informacion["foto"])
            if informacion.get("descripcion"):
                estudiantes.descripcion = informacion["descripcion"]
            estudiantes.save()
            return render(request, "AppProyecto/padre.html")
    else:
        miFormulario = EstudiantesForm()
    return render(request, "AppProyecto/Estudiantesform.html", {"miFormulario": miFormulario})

@login_required
def busquedacamada(req):
    return render(req, "AppProyecto/busquedacamada.html")

@login_required
def resultadobusqueda(request):
    return render(request, 'AppProyecto/resultadobusqueda.html')

@login_required
def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppProyecto/resultadobusqueda.html", {"curso": curso, "camada": camada})
    else:
        respuesta = "No enviaste ningun dato"
        return HttpResponse(respuesta)
