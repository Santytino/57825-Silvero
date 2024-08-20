from AppProyecto import views
from django.urls import path


urlpatterns = [
    path('padre/', views.padre, name='padre'),

]