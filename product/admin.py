from django.contrib import admin
from .models import Category, Product, Marca, Color, Size, ProductStock,ProductImage


@admin.register(Color)  # Registrar Color una vez
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_value')  # Mostrar estos campos en la lista
    search_fields = ['name']  # Agregar barra de búsqueda


@admin.register(Size)  # Registrar Size una vez
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Mostrar nombres en la lista
    search_fields = ['name']  # Agregar barra de búsqueda


class ProductStockInline(admin.TabularInline):  # Inline para ProductStock
    model = ProductStock
    extra = 1  # Número de filas vacías adicionales
    min_num = 1  # Mínimo de combinaciones requeridas
    autocomplete_fields = ['color', 'size']  # Mejor experiencia de selección
    fields = ('color', 'size', 'stock')  # Campos visibles en el inline


@admin.register(Product)  # Registrar Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'price', 'is_active', 'total_stock']
    search_fields = ['name', 'sku']
    list_filter = ['is_active', 'categories', 'marca']
    inlines = [ProductStockInline]  # Mostrar ProductStock en el admin de Product

    def total_stock(self, obj):
        """Calcula el stock total para mostrarlo en la lista."""
        return sum(stock_item.stock for stock_item in obj.stocks.all())
    total_stock.short_description = "Stock Total"  # Texto para la columna


@admin.register(Marca)  # Registrar Marca
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductStock)
