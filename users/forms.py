from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = 'Enter your name'
        self.error_messages['invalid_login'] = 'INVALID CREDENTIALS!!! Enter your name you used to create an account. \
            Name and password may be case-sensitive.'
        self.fields['username'] = UsernameField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
        

class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

