from typing import Any
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

class CustomUserCreationForm(UserCreationForm):

    def save(self, commit = True) -> Any:
       user = super().save(commit=False)
       username = slugify(self.cleaned_data['email'].split('@')[0])
       user.username = username
       if commit:
            user.save()
       return user
    

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ['username']
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'role')
        labels = {
            'email': 'Correo electrónico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
            'role': 'Rol',

        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),   
        }