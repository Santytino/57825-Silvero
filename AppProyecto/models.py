from django.db import models

# Create your models here.

class Curso(models.Model):
    cursos = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Curso {self.curso} y camada {self.camada}"

class Estudiante(models.Model):
    nombreapellidoEst = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombreapellidoEst} se añadio y su email es {self.email}"

class Profesor(models.Model):
    nombreapellidoProf = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombreapellidoProf} con la profesion de {self.profesion}, se añadió con el email {self.email}"