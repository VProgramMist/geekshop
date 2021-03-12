from django import forms

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from authapp.widgets import CustomImageWidget


class UserAdminRegisterForm(UserRegisterForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'avatar', 'email', 'password1', 'password2')
        widgets = {
            'avatar': CustomImageWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)


class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
