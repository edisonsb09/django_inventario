from django.contrib import admin
from .models import Categoria, Producto, Proveedor, OrdenCompra, DetalleOrdenCompra

# Registrar los modelos en el panel administrativo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'cantidad_disponible']
    list_filter = ['categoria', 'precio']
    search_fields = ['nombre', 'categoria__nombre']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono', 'email']
    search_fields = ['nombre', 'email']

@admin.register(OrdenCompra)
class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ['proveedor', 'fecha', 'total']
    list_filter = ['proveedor', 'fecha']
    search_fields = ['proveedor__nombre']

@admin.register(DetalleOrdenCompra)
class DetalleOrdenCompraAdmin(admin.ModelAdmin):
    list_display = ['orden', 'producto', 'cantidad', 'precio_unitario']
    list_filter = ['orden', 'producto']
    search_fields = ['orden__proveedor__nombre', 'producto__nombre']
