from django import forms
from .models import Lote
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = [
            'id_lote',
            'analisis_espectrometrico',
            'tolerancia_geometrica',
            'numero_partes',
            'prueba_dureza_tension',
            'evidencia_fotografica',
            'plano_original',
        ]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'empresa')
