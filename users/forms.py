from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get['username']
        if User.objects.filter(username=username).exists(): # -> true yoki false qaytaradi
            raise forms.ValidationError('bunday username ga ega foydalanuvchi topilmadi')
        return username
    
    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data["password"]
        if username:
            user = User.objects.filter(username=username)
            if user:
                if not user.check_password(password):
                    raise forms.ValidationError("parol noto'gri")
        return password

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120, required=True, label='Login')
    password = forms.CharField(max_length=100,
                        widget=forms.PasswordInput(attrs={'class': 'special'}))
    password_confirmation = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    # password_confirmation.widget.attrs.update({'class': 'special'})
    # password_confirmation.widget.attrs.update(size='40')

    def clean_password(self):
        parol = self.cleaned_data['password']
        if len(parol) < 7:
            raise forms.ValidationError('Parol kamida 7ta belgidan iborat bo\'lishi lozim')
        if parol.isnumeric():
            raise forms.ValidationError('Parolda kamida bitta harf yoki belgi ishtirok etishi lozim')
        if parol.isalpha():
            raise forms.ValidationError('Parolda kamida bitta raqam ishtirok etishi lozim')
        return parol

    def clean_password_confirmation(self):
        password = self.data['password']
        confirm_password = self.cleaned_data['password_confirmation']
        if password != confirm_password:
            raise forms.ValidationError('Tasdiqlash paroli notogri')
        return confirm_password

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already registered on our platform')
        return username
