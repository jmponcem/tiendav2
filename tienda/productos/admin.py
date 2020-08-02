from django.contrib import admin
from .models import Producto, Comentario, ImagenesProducto, CarritoCompra

@admin.register(Producto, Comentario, ImagenesProducto, CarritoCompra)
class AuthorAdmin(admin.ModelAdmin):
    pass

