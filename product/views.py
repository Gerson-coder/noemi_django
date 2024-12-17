from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category

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