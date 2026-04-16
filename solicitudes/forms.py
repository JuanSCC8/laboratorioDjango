from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'nombre_solicitante': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ingrese nombre completo',
            }),
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej: 12345678A',
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'correo@ejemplo.com',
            }),
            'telefono_contacto': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej: 3001234567',
            }),
            'tipo_solicitud': forms.Select(attrs={
                'class': 'form-input',
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Asunto de la solicitud',
            }),
            'descripcion_detallada': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 5,
                'placeholder': 'Describa detalladamente su solicitud...',
            }),
            'fecha_solicitud': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'archivo_adjunto': forms.ClearableFileInput(attrs={
                'class': 'form-file',
            }),
        }
