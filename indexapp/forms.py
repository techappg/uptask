from django import forms

from taskapp.models import User


class LoginForm(forms.Form):
    username_or_email = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter username or email','class':'form-control', }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password','class':'form-control',}))

