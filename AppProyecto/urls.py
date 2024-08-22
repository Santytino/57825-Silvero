from AppProyecto import views
from django.urls import path


urlpatterns = [
    path('padre/', views.padre, name='padre'),
    path('curso/', views.curso, name='curso'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursoform/', views.cursoform, name='cursoform'),
    path('estudiantesform/', views.estudiantesform, name='estudiantesform'),
    path('profesoresform/', views.profesoresform, name='profesoresform'),
    path('busquedacamada/', views.busquedacamada, name='busquedacamada'),
    path('resultadobusqueda/', views.resultadobusqueda, name='resultadobusqueda'),
    path('buscar/', views.buscar, name='buscar'),

]