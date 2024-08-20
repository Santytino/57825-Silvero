from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Estudiante, Profesor


# Create your views here.

def padre(req):
    return render(req, 'appproyecto/padre.html')

def cursos(req):
    return render(req, 'templates/appproyecto/cursos.html')