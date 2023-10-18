from django.contrib import admin
from AppUsuarios.models import Imagen

# Register your models here.

@admin.register(Imagen)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ("user", "imagen")