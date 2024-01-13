from django import forms
from .models import Contactos

class ContatcForm(forms.ModelForm):

    class Meta:
        model = Contactos
        fields = ['name', 'email', 'phone']

        labels = {
            'name': 'Nombre del contacto',
            'email': 'Correo electronico',
            'phone': 'Telefono'
        }, 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }




