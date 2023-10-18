from django.contrib import admin
from AppBookrealm.models import *

# Register your models here.



@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "stock", "precio", "oferta", "autor", "editorial")

    ordering = ("titulo", )
    search_fields = ("oferta", "editorial")


# Laura - dsfk567E*
# acotina890 - aco.yardanps3