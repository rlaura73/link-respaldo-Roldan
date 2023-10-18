from django.urls import path
from django.contrib.auth.views import LogoutView
from AppUsuarios import views


urlpatterns = [
    path('perfil/', views.pag_usuario, name="PagUsuario"),
    path('inicio-sesion/', views.login_request, name="Login"),
    path('registro/', views.registrar_usuario, name="Registro"), 
    path('logout/', LogoutView.as_view(template_name = "AppBook/index.html"), name="Logout"),
    path('editar-perfil/', views.editar_usuario, name="EditarPerfil")
]
