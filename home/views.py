from django.shortcuts import render
from product.models import Category

# Create your views here.


def home(request):

    categories = Category.objects.filter(id__in=[1,2,3,4,5,6,7,8,9])
    
    

    context ={
        'category_1': categories.filter(id=1).first(),
        'category_2': categories.filter(id=2).first(),
        'category_3': categories.filter(id=3).first(),
        'category_4': categories.filter(id=4).first(),
        'category_5': categories.filter(id=5).first(),
        'category_6': categories.filter(id=6).first(),
        'category_7': categories.filter(id=7).first(),
        'category_8': categories.filter(id=8).first(),
        'category_9': categories.filter(id=9).first(),
       
        
    }

    return render(request,'index.html', context)
