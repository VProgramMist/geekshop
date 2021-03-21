from django.urls import path, re_path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.ProductsView.as_view(), name='index'),
   re_path(r'(?:category-(?P<cat_key>\d+)/)?(?:(?P<page>\d+)/)?$', mainapp.ProductsView.as_view(), name='products'),
]