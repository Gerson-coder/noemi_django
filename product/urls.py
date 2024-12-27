
from django.urls import path
from .views import products_girls, products_boys, product_store, product_detail


urlpatterns = [
    path('products-girls',products_girls,name= 'girls'),
    path('products-boys',products_boys,name= 'boys'),
    path('category/<int:category_id>/', product_store, name='product_category'),
    path('product-detail/<int:product_id>/',product_detail,name='product_detail')

]
