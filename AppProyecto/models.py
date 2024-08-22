from django.db import models

# Create your models here.

class Curso(models.Model):
    curso = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiantes(models.Model):
    nombreapellidoEst = models.CharField(max_length=50)
    email = models.EmailField()

class Profesores(models.Model):
    nombreapellidoProf = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)