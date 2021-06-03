from django import forms
from django.forms.widgets import PasswordInput


class SignUpForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    organization = forms.CharField(label="Organization", max_length=100)
    age = forms.IntegerField(label="Age", max_value=100, min_value=13)
    password = forms.CharField(
        label="Password", max_length=20, min_length=7)
