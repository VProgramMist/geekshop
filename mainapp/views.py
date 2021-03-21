from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.list import ListView

from mainapp.models import Product, ProductCategory


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


class ProductsView(ListView):
    model = Product
    template_name = 'mainapp/products.html'

    def __init__(self):
        super(ProductsView, self).__init__()
        self.page = 1
        self.cat_key = None

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        if self.kwargs.get('cat_key'):
            self.queryset = queryset.filter(categories=self.kwargs.get('cat_key'))
            self.cat_key = self.kwargs.get('cat_key')
        else:
            self.queryset = queryset.all()
        if self.kwargs.get('page'):
            self.page = self.kwargs.get('page')
        else:
            self.page = 1

    def get_context_data(self, **kwargs):
        kwargs = super(ProductsView, self).get_context_data(**kwargs)
        kwargs.update({
            'title': 'GeekShop - Каталог',
            'categories': ProductCategory.objects.all(),
            'cur_cat': self.cat_key,
        })
        paginator = Paginator(self.queryset, per_page=3)
        products_paginator = paginator.page(self.page)
        kwargs.update({'products': products_paginator})

        return kwargs
