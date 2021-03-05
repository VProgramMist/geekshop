from django.urls import path

import basketapp.views as basketapp

app_name = 'authapp'

urlpatterns = [
   path('login-add/<int:product_id>/', basketapp.basket_add, name='baket_add'),
]