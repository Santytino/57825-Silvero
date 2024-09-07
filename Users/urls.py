from django.urls import path
from Users import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='AppProyecto/padre.html'), name="Logout"),
    path('edit/', views.editar_perfil, name="EditarPerfil"),
    path('cambiar_pass/', views.CambiarContrasenia.as_view(), name="CambiarPass")
]
