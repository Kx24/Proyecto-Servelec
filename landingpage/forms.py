# Landingpage/forms.py
from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-lg border border-gray-300 bg-white px-4 py-3 text-servelec-dark placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-servelec-primary',
            'placeholder': 'Ej. Nombre Apellido'
        })
    )

    correo = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'block w-full rounded-lg border border-gray-300 bg-white px-4 py-3 text-servelec-dark placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-servelec-primary',
            'placeholder': 'Ej. nombre@correo.com'
        })
    )

    telefono = forms.CharField(
        max_length=20,
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-lg border border-gray-300 bg-white px-4 py-3 text-servelec-dark placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-servelec-primary',
            'placeholder': 'Ej. +56 9 1234 5678'
        })
    )

    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'block w-full rounded-lg border border-gray-300 bg-white px-4 py-3 text-servelec-dark placeholder-gray-400 resize-none focus:outline-none focus:ring-2 focus:ring-servelec-primary',
            'placeholder': 'Describe brevemente tu requerimiento...'
        })
    )

    # Validación personalizada opcional
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.startswith('+56'):
            raise forms.ValidationError("El teléfono debe comenzar con +56")
        return telefono