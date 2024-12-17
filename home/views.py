from django.shortcuts import render
from product.models import Category

# Create your views here.


def home(request):

    categories = Category.objects.filter(id__in=[1,2,3,4,5,6,7,8,9])
    
    

    context ={
        'categories':categories,
        
    }

    
    
    return render(request,'index.html', context)
