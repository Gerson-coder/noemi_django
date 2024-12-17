from django.shortcuts import render

# Create your views here.


def home(request):
    
    return render(request, 'index.html')

def product_store(request, category_id):
    # Aquí puedes obtener los productos según la categoría
    # Por ejemplo:
    categories = {
        1: {'name': 'tops', 'template': 'categories/tops.girls.html'},
        2: {'name': 'dresses', 'template': 'categories/dresses_girls.html'},
       
    }
    
    category = categories.get(category_id, {'name': 'Default', 'template': 'categories/default.html'})# pone como default si no encuentra
    
    context = {
        'category_name': category['name'],
        # Aquí puedes agregar más datos para la vista
    }
    
    return render(request, category['template'], context)
