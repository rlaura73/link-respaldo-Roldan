from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from AppUsuarios.forms import IniciarSesion, RegistroUsuario, EditarUsuario
from AppUsuarios.models import Imagen

# Create your views here.






def pag_login(request):
    return render(request, "AppUsers/login.html")


@login_required
def pag_usuario(request):
    return render(request, "AppUsers/usuario.html")





def login_request(request):
    if request.method == "POST":
        # form = AuthenticationForm(request, data = request.POST)
        form = IniciarSesion(request, data = request.POST)

        print(form)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = clave)

            if usuario is not None:
                login(request, user)

                return render(request, "AppBook/index.html")
            
            else:
                return render(request, "AppUsers/mensaje.html", {"mensaje":"Error, datos incorrectos"})
            
        else:
            return render(request, "AppUsers/mensaje.html", {"mensaje":"Error, formulario ivalido"})

    # form = AuthenticationForm()
    form = IniciarSesion()

    return render(request, "AppUsers/login.html", {"form":form})





def registrar_usuario(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = RegistroUsuario(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()

            return render(request, "AppUsers/login.html")
        
        else:
            print("Formulario invalido")

    else:
        # form = UserCreationForm()
        form = RegistroUsuario()

    return render(request, "AppUsers/registro.html", {"form":form})







@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == "POST":
        form = EditarUsuario(request.POST, request.FILES)

        print(form)

        if form.is_valid():
            info = form.cleaned_data

            if info["password1"] != info["password2"]:
                datos = {
                    "first_name": usuario.first_name,
                    "email": usuario.email
                }
                form = EditarUsuario(initial=datos)
            
            else:
                usuario.email = info["email"]
                usuario.first_name = info["first_name"]
                usuario.last_name = info["last_name"]
                usuario.password1 = info["password1"]
                usuario.password2 = info["password2"]
                usuario.save()


                try:
                    avatar = Imagen.objects.get(user=usuario)
                except Imagen.DoesNotExist:
                    avatar = Imagen(user=usuario, imagen=info["imagen"])
                    avatar.save()
                else:
                    avatar.imagen = info["imagen"]
                    avatar.save()

                return render(request, "AppUsers/usuario.html")
        
    else:
        datos = {
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name
        }

        form = EditarUsuario(initial=datos)

    
    return render(request, "AppUsers/editarPerfil.html", {"form":form})



    