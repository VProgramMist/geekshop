from django.shortcuts import HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket


def basket_add(request, product_id=None):
    product = Product.objects.get(id=product_id)
    basket_elements = Basket.objects.filter(user=request.user, product=product)

    if not basket_elements.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity = 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = basket_elements.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


