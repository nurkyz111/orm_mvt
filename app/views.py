from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'home.html',
                  {'categories': categories,
                   'products': products})


def category_detail(request, _id):
    category = get_object_or_404(Category, id=_id)
    products = Product.objects.filter(category=category)
    return render(request, 'categories/detail.html', {'category': category,
                                                      'products': products})


def product_detail(request, _id):
    product = get_object_or_404(Product, id=_id)
    return render(request, 'categories/product.html',
                  {'product': product})
