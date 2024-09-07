from django.shortcuts import render
from .models import Curso, Estudiantes
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def padre(req):
    return render(req, 'AppProyecto/padre.html')


class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppProyecto/Vista_Clase/curso_list.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        for curso in self.get_queryset():
            print(f"Curso: {curso.curso}, Camada: {curso.camada}")
        return response


class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "AppProyecto/Vista_Clase/curso_detalle.html"


class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    template_name = "AppProyecto/Vista_Clase/curso_form.html"
    fields = ["curso", "camada"]
    success_url = reverse_lazy("List")


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = reverse_lazy("List")
    fields = ["curso", "camada"]
    template_name = "AppProyecto/Vista_Clase/curso_edit.html"


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy("List")
    template_name = 'AppProyecto/Vista_Clase/curso_confim_delete.html'
    

class EstudiantesListView(LoginRequiredMixin, ListView):
    model = Estudiantes 
    template_name = "AppProyecto/Vista_Clase/est_list.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        for estudiante in self.get_queryset():
            print(f"Nombre: {estudiante.nombreapellidoEst}, Email: {estudiante.email}")
        return response

class EstudiantesDetailView(LoginRequiredMixin, DetailView):
    model = Estudiantes
    template_name = "AppProyecto/Vista_Clase/est_detalle.html"


class EstudiantesListView(LoginRequiredMixin, ListView):
    model = Estudiantes
    template_name = "AppProyecto/Vista_Clase/est_list.html"

class EstudiantesDetailView(LoginRequiredMixin, DetailView):
    model = Estudiantes
    template_name = "AppProyecto/Vista_Clase/est_detalle.html"

class EstudiantesCreateView(LoginRequiredMixin, CreateView):
    model = Estudiantes
    fields = ['nombreapellidoEst', 'email', 'foto', 'descripcion']
    template_name = "AppProyecto/Vista_Clase/est_form.html"
    success_url = reverse_lazy('ListEst')