from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True,help_text='Requerido. Agregue una dirección de correo valida', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Correo Electronico'}))
    nombres = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombres'}))
    apellidos = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Apellidos'}))
    cedula = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Cedula Profesional'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder':'Confirmar Contraseña'}))

    class Meta:
        model = Account
        fields = ("email","nombres","apellidos","cedula","password1","password2")