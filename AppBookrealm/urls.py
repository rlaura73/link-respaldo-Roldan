from django.urls import path
from AppBookrealm import views

urlpatterns = [
    path('', views.pag_inicio, name="PagInicio"),
    path('ofertas/', views.ListaOfertas.as_view(), name="PagOfertas"),
    path('discusiones/', views.pag_discusiones, name="PagDisc"),
    path('about/', views.pag_about, name="PagAbout"),
    path('compras/', views.pag_compras, name="PagCompras"),
]

urlpatterns += [
    path('libros/', views.ListaLibros.as_view(), name="PagLibros"),
    path('libros/detalle-libro/<int:pk>/', views.DetalleLibro.as_view(), name="DetalleLibro"),
    path('libros/nuevo-libro/', views.AgregarLibro.as_view(), name="AgregarLibro"),
    path('libros/modificar-libro/<int:pk>/', views.ModificarLibro.as_view(), name="EditarLibro"),
    path('libros/eliminar-libro/<int:pk>/', views.EliminarLibro.as_view(), name="EliminarLibro"),
]