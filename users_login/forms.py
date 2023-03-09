from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'field login', 'placeholder': 'Username', 'style': 'position: absolute; width: 30%; height: 38px; left: 35%; top: 35%;'})
        self.fields['password'].label = ''
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'field password', 'placeholder': 'Password', 'style': 'position: absolute; width: 30%; height: 38px; left: 35%; top: 50%;'})
