from django.urls import path

import basketapp.views as basketapp

app_name = 'authapp'

urlpatterns = [
   path('basket-add/<int:product_id>/', basketapp.basket_add, name='basket_add'),
   path('basket-delete/<int:id>/', basketapp.basket_delete, name='basket_delete'),
]