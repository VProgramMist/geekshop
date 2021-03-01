from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request, cat_key=None):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all() if cat_key is None else Product.objects.filter(categories=cat_key),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
