from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Nombre", max_length=50, unique=True)
    description = models.TextField("Descripción", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Marca(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField("Nombre",max_length=20,blank=False,null=False)
     logo = models.ImageField(upload_to="logo_marca/")
     created_at = models.DateField(auto_now=False, auto_now_add= True)
    
     class Meta:
          
          verbose_name = " Marca"
          verbose_name_plural = "Marcas"
    
     def  __str__(self):
        return self.name
     
class Color(models.Model):
    name = models.CharField("Color", max_length=20, unique=True)
    hex_value = models.CharField("Código HEX", max_length=7, blank=True, null=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField("Talla", max_length=5, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
   
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre',max_length=100,blank=False,null=False)
    description = models.TextField("Description")
    sku = models.CharField("SKU",max_length=20,blank=False,null=False)
    material = models.CharField("Material", max_length=50, blank=True, null=True)
    collection = models.CharField("Colección", max_length=30, blank=True, null=True)
    price = models.DecimalField("Precio",max_digits= 10, decimal_places = 2, blank=False,null=False)
    
    season = models.CharField("Temporada",max_length=15,
    choices=[('Spring', 'Primavera'), ('Summer', 'Verano'),  ('Fall', 'Otoño'),
            ('Winter', 'Invierno'),], blank=True,  null=True,)
    gender = models.CharField(
    "Género",max_length=10,
    choices=[('Boy', 'Niño'),('Girl', 'Niña'), ('Women', 'Mujer'), ('Unisex', 'Unisex')],blank=True,null=True,   
)
    categories = models.ManyToManyField(Category, related_name='products')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, blank= True, null=True)
    discount_price = models.DecimalField("Precio con descuento", max_digits=10, decimal_places = 2,blank=True,null=True)
    sold_count = models.IntegerField("Cantidad vendida", blank=True, null=True)
    is_featured = models.BooleanField("Es destacado", default=False)
    image = models.ImageField(upload_to="Product")
    created_at = models.DateField(auto_now=False, auto_now_add= True)
    updated_at = models.DateField(auto_now=True,auto_now_add=False)
    is_active = models.BooleanField("Está activo", default=True)
    average_rating = models.FloatField("Calificación promedio", default=0.0)
    review_count = models.PositiveIntegerField("Cantidad de reseñas", default=0)
    slug = models.SlugField(unique=True, blank=True, null=True)
    discount_start_date = models.DateField("Inicio del descuento", blank=True, null=True)
    discount_end_date = models.DateField("Fin del descuento", blank=True, null=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    def __str__(self):
        return f' {self.name} - {self.marca} '
    
    def clean(self):
        if self.discount_start_date and self.discount_end_date:
            if self.discount_start_date > self.discount_end_date:
                raise ValidationError("La fecha de inicio del descuento no puede ser posterior a la fecha de finalización.")
    
    
    def save(self, *args, **kwargs):
    # Esta es la definición del método save que sobrescribe el método save original de Django
    # *args y **kwargs permiten pasar argumentos posicionales y de palabra clave adicionales
    
        if not self.slug:
        # Verifica si el campo slug está vacío
        # Si está vacío, significa que es un nuevo producto o no tiene slug asignado
        
            self.slug = slugify(self.name)
        # Crea un slug a partir del nombre del producto usando la función slugify
        # Por ejemplo: "Zapatos Deportivos" -> "zapatos-deportivos"
        # slugify convierte espacios en guiones, elimina caracteres especiales y convierte a minúsculas
    
        super(Product, self).save(*args, **kwargs)
    # Llama al método save original de la clase padre (Model)
    # Esto guarda efectivamente el objeto en la base de datos

    
    
class ProductStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stocks")
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField("Cantidad disponible", default=0)
    
    class Meta:
        unique_together = ('product', 'color', 'size')  # Evita combinaciones duplicadas
    
    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"