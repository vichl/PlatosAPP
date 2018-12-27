from django.contrib import admin

from .models import Familia, Plato, Producto, Ingrediente, Categoria

# Register your models here.

admin.site.register(Familia)
admin.site.register(Categoria)


class IngredienteInline(admin.TabularInline):
    model = Ingrediente
    extra = 0


class ProductoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'familia', 'precio', 'unidades']}),
        ('Opcional', {'fields': ['marca', 'proveedor', 'observaciones']}),
    ]
    list_display = ('familia', 'nombre', 'marca', 'proveedor')
    list_filter = ['familia']


class PlatoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'categoria']}),
        ('Opcional', {'fields': ['observaciones']}),
    ]
    inlines = [IngredienteInline]
    list_display = ('categoria', 'nombre')
    list_filter = ['categoria']


admin.site.register(Plato, PlatoAdmin)
admin.site.register(Producto, ProductoAdmin)

