from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=PasswordInput)