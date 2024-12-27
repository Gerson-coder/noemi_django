from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category, Product

# Create your views here.


def products_girls(request):

    return render(request,'girls.html')

def products_boys(request):

    return render(request,'boys.html')


def product_store(request, category_id):
    # Aquí puedes obtener los productos según la categoría
    # Por ejemplo:
    categoria  = get_object_or_404(Category,id = category_id)
    

    print(f'Category id received: {category_id}'),
    print(f'Category name: {Category.name}'),
    print(f'Category id type: {type(category_id)}'),
   # Pasa el contexto al template
    context = {
      
        'category_name': categoria.name,
    }
    
    # Renderiza el template correspondiente
    return render(request, categoria.template, context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_images= product.images.all()
    product_stocks = product.stocks.all()  # Obtener todas las combinaciones de stocks

     # Filtrar tallas disponibles
    available_sizes = product.stocks.filter(stock__gt=0).values('size__id', 'size__name')

    
       # Diccionario con disponibilidad de combinaciones color-talla
    stocks = {
        f"{stock.color.id}-{stock.size.id}": stock.stock > 0
        for stock in product_stocks
    }

    context = {
        'product_id': product,
        'product_stocks': product_stocks,
        'product_images': product_images,
         'available_sizes': available_sizes,  # Pasar tallas disponibles al contexto
        'stocks': stocks,
    }

    return render(request, 'product_detail.html', context)