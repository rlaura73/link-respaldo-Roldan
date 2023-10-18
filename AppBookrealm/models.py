from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.CharField(max_length=10)
    oferta = models.CharField(max_length=5)

    def __str__(self):
        return {self.titulo}


# class Compra(models.Model):
#     usuario = models.CharField(max_length=100)
#     libro = models.CharField(max_length=200)
#     oferta = models.CharField(max_length=5)
#     precio = models.CharField(max_length=10)
#     pago = models.CharField(max_length=50)
#     fecha = models.DateField()



# class Usuario(models.Model):
#     usuario = models.CharField(max_length=100)
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     correo = models.CharField(max_length=100)
#     clave = models.CharField(max_length=100)