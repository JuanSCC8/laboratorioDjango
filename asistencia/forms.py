from django import forms
from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        widgets = {
            'nombre_completo': forms.TextInput(attrs={
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
            'fecha_asistencia': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'hora_ingreso': forms.TimeInput(attrs={
                'class': 'form-input',
                'type': 'time',
            }),
            'hora_salida': forms.TimeInput(attrs={
                'class': 'form-input',
                'type': 'time',
            }),
            'presente': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': 'Observaciones adicionales (opcional)',
            }),
        }
