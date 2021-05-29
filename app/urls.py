from django.urls import path
from .views import home, category_detail, product_detail

urlpatterns = [
    path('category/<slug:slug>', category_detail, name='category'),
    path('product/<int:_id>', product_detail, name='product_detail'),
    path('', home),
]