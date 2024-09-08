from AppProyecto import views
from django.urls import path
from AppProyecto import views_clases

urlpatterns = [
    path('', views.padre, name='padre'),
    path('curso/', views.curso, name='curso'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursoform/', views.cursoform, name='cursoform'),
    path('estudiantesform/', views.estudiantesform, name='estudiantesform'),
    path('profesoresform/', views.profesoresform, name='profesoresform'),
    path('busquedacamada/', views.busquedacamada, name='busquedacamada'),
    path('resultadobusqueda/', views.resultadobusqueda, name='resultadobusqueda'),
    path('buscar/', views.buscar, name='buscar'),
    path('nosotros/', views.nosotros, name='nosotros'),

]

urls_vistas_clases = [
    path('clases/lista/', views_clases.CursoListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/', views_clases.CursoDetailView.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.CursoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>/', views_clases.CursoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>/', views_clases.CursoDeleteView.as_view(), name='Delete'),
    path('clases/lista_est/', views_clases.EstudiantesListView.as_view(), name='ListEst'),
    path('clases/detalle_est/<int:pk>/', views_clases.EstudiantesDetailView.as_view(), name='DetailEst'),
    path('clases/nuevo_est/', views_clases.EstudiantesCreateView.as_view(), name='NewEst'),
]

urlpatterns += urls_vistas_clases