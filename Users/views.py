from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserEditForm
from .models import Imagen
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        form.fields['username'].label = "Usuario"
        form.fields['password'].label = "Contraseña"

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppProyecto/padre.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    form.fields['username'].label = "Usuario"
    form.fields['password'].label = "Contraseña"
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppProyecto/padre.html")
        else:
            msg_register = "Usuario y contraseña similares"
    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})

def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if Imagen.objects.filter(user=usuario).exists():
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()
                else:
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()
            miFormulario.save()
            return render(request, "AppProyecto/padre.html")
    else:
        miFormulario = UserEditForm(instance=usuario)
    return render(request, "users/editar_perfil.html", {"mi_form": miFormulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")
    
    
    
    
# def editar_perfil(request):
#     usuario = request.user
#     if request.method == 'POST':
#         miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

#         if miFormulario.is_valid():
#             if miFormulario.cleaned_data.get('imagen'):
#                 if Imagen.objects.filter(user=usuario).exists():
#                     usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
#                     usuario.imagen.save()
#                 else:
#                     avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
#                     avatar.save()
#             miFormulario.save()
#             return render(request, "AppProyecto/padre.html")
#     else:
#         miFormulario = UserEditForm(instance=usuario)
#     return render(request, "users/editar_perfil.html", {"mi_form": miFormulario, "usuario": usuario})