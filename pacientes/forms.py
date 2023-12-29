from django import forms
from .models import Paciente
from django.core.validators import RegexValidator

class PacienteForm(forms.ModelForm):

    identification_validator = RegexValidator(
        regex=r'^[0-9]{8}$',
        message='El documento de identidad debe tener 8 dígitos'
    )

    class Meta:
        model = Paciente
        fields = ['large_name', 'identification', 'address', 'phone']
        labels = {
            'large_name': 'Nombre del paciente',
            'identification': 'Documento de identidad',
            'address': 'Dirección',
            'phone': 'Teléfono',
        }
        widgets = {
            'large_name': forms.TextInput(attrs={'class': 'form-control'}),
            'identification': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

        