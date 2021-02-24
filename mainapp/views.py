from django.shortcuts import render
import json
import os

module_dir = os.path.dirname(__file__)


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    import os
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    context = {'title': 'GeekShop - Каталог'}
    context.update(json.load(open(file_path, encoding='utf-8')))
    return render(request, 'mainapp/products.html', context)
