from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket
from authapp.models import User


class UserLoginView(LoginView):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm


class UserCreateView(CreateView):
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:login')


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('index')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('auth:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        kwargs = super(UserUpdateView, self).get_context_data(**kwargs)
        kwargs.update({'basket': Basket.objects.filter(user=self.request.user)})
        return kwargs
