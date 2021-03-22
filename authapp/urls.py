from django.urls import path
from django.contrib.auth.decorators import login_required

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
   path('login/', authapp.UserLoginView.as_view(), name='login'),
   path('register/', authapp.UserCreateView.as_view(), name='register'),
   path('logout/', authapp.UserLogoutView.as_view(), name='logout'),
   path('profile/', login_required(authapp.UserUpdateView.as_view()), name='profile'),
]