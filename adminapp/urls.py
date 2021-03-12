from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
   path('', adminapp.index, name='index'),
   path('users/', adminapp.admin_users, name='admin_users'),
   # path('basket-delete/<int:id>/', adminapp.admin_users_create, name='admin_users_create'),
   # path('basket-edit/<int:id>/<int:quantity>/', adminapp.admin_users_update, name='admin_users_update'),
   # path('basket-edit/<int:id>/<int:quantity>/', adminapp.admin_users_delete, name='admin_users_delete'),
]