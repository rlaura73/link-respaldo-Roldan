from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from AppBookrealm.models import Libro
from AppBookrealm.forms import *
from AppUsuarios.models import Imagen



# Create your views here.

def pag_inicio(request):

    imgs = Imagen.objects.filter(user=request.user.id)

    return render(request, "AppBook/index.html")

@login_required
def pag_compras(request):
    return render(request, "AppBook/compras/compras.html")

def pag_about(request):
    return render(request, "AppBook/about.html")

def pag_discusiones(request):
    return render(request, "AppBook/discusiones/discusiones.html")




# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------


class ListaLibros(ListView):
    model = Libro
    template_name = "AppBook/libros/libros.html"

class ListaOfertas(ListView):
    model = Libro
    template_name = "AppBook/ofertas/ofertas.html"


class DetalleLibro(DetailView):
    model = Libro
    template_name = "AppBook/libros/libro_detalle.html"



class AgregarLibro(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = "AppBook/libros/libro_form.html"
    success_url = reverse_lazy("PagLibros")
    fields = ["titulo", "autor", "editorial", "stock", "precio", "oferta"]


class ModificarLibro(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "AppBook/libros/libro_form.html"
    success_url = reverse_lazy("PagLibros")
    fields = ["titulo", "autor", "editorial", "stock", "precio", "oferta"]


class EliminarLibro(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "AppBook/libros/libro_confirm_delete.html"
    success_url = reverse_lazy("PagLibros")
