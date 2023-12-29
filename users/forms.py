from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from users.models import User


class FormClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(FormClassMixin, UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name in ['password1', 'password2']:
                field.widget.attrs['placeholder'] = 'введите пароль'

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'введите email',
                    'data-form-field': 'email',
                    'value': '',
                    'id': 'email-contact-form-2-tZlMaS1ydf',
                }
            )
        }


class UserProfileForm(FormClassMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country', 'birthday')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserAuthenticationForm(FormClassMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')
