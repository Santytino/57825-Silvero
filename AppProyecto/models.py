from django.db import models
from django.urls import reverse

# Create your models here.

class Curso(models.Model):
    curso = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f"Curso: {self.curso} - Camada: {self.camada}"

class Estudiantes(models.Model):
    nombreapellidoEst = models.CharField(max_length=50)
    email = models.EmailField()
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"Nombre: {self.nombreapellidoEst} - Email: {self.email}"
    
    def get_absolute_url(self):
        return reverse('detalle_est', kwargs={'pk': self.pk})


class Profesores(models.Model):
    nombreapellidoProf = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombreapellidoProf} - Email: {self.email} - Profesion: {self.profesion}"
