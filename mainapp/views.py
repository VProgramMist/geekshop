from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from mainapp.models import Product, ProductCategory


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request, cat_key=None, page=1):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    products = Product.objects.filter(categories=cat_key) if cat_key else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except InvalidPage:
        products_paginator = paginator.page(1)
    context.update({'products': products_paginator})

    return render(request, 'mainapp/products.html', context)
